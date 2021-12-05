"""Клиент"""
import json
import socket
import sys
import time

from collective.general_func import send_message, get_message
from collective.settings import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, DEFAULT_IP_ADDRESS, \
    DEFAULT_PORT, RESPONSE, ERROR
import logging
import logs.client_log_config
from decorators import log

logger_client = logging.getLogger('app.client')


@log
def create_presence(account_name='Guest'):
    """
    Функция генерирует запрос о присутсвии клиента
    """
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    logger_client.debug(f'Сформировано {PRESENCE} сообщение для пользователя {account_name}')
    return out


@log
def process_ans(message):
    """
    Функция разбирает ответ сервера
    """
    logger_client.debug(f'Разбор сообщения от сервера: {message}')
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


def main():
    """
    Загружает параметры командной строки
    """
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        # print('В качестве порта может быть указано только число в диапазоне 1025 - 65534')
        logger_client.critical('В качестве порта может быть указано только число в диапазоне 1025 - 65534')
        sys.exit(1)

    # Инициализация сокета и обмен

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    message_to_server = create_presence()
    send_message(transport, message_to_server)
    try:
        answer = process_ans(get_message(transport))
        # print(answer)
        logger_client.info(answer)
    except (ValueError, json.JSONDecodeError):
        # print('Не удалось декодировать сообщение сервера.')
        logger_client.critical('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
