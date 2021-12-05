"""Сервер"""

import socket
import sys
import json
from collective.settings import ACTION, ACCOUNT_NAME, RESPONSE, PRESENCE, \
    TIME, USER, ERROR, DEFAULT_PORT, RESPONSEDEFAULT_IP_ADDRESS, MAX_CONNECTIONS
from collective.general_func import get_message, send_message
import logging
import logs.server_log_config
from decorators import log

logger_serv = logging.getLogger('app.server')


@log
def process_client_message(message):
    """
    Обработчик сообщений от клиента
    """
    logger_serv.debug(f'Разбор сообщения от клиента : {message}')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSEDEFAULT_IP_ADDRESS: 400,
        ERROR: 'Bad Request'
    }


@log
def main():
    """
    Загрузка параметров командной строки, если нет параметров, то задаем значения по умолчанию.
    Сначала обрабатываем порт:
    server.py -p 8888 -a 127.0.0.1
    """
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
            if listen_port < 1024 or listen_port > 65535:
                raise ValueError
    except IndexError:
        # print("После параметра '-p' необходимо указать номер порта.")
        logger_serv.info("После параметра '-p' необходимо указать номер порта.")
        sys.exit(1)

    # Затем загружаем какой адрес слушать
    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''

    except IndexError:
        # print("После параметра '-a' необходимо указать адрес, который будет слушать сервер.")
        logger_serv.info("После параметра '-a' необходимо указать адрес, который будет слушать сервер.")
        sys.exit(1)

    # Готовим сокет

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # transport.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    transport.bind((listen_address, listen_port))

    # Слушаем порт

    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        try:
            message_from_client = get_message(client)
            # print(message_from_client)
            logger_serv.info(message_from_client)
            response = process_client_message(message_from_client)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            # print('Принято не корректное сообщение от клиента.')
            logger_serv.critical('Принято не корректное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()
