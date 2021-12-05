import json
from collective.settings import MAX_PACKAGE_LENGTH, ENCODING
import logging
import logs.server_log_config
from decorators import log

logger_g_func = logging.getLogger('app.g_func')


@log
def get_message(sock):
    """
    Прием и кодирование сообщения
    """
    encoded_response = sock.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            logger_g_func.debug(response)
            return response
        raise ValueError
    raise ValueError


@log
def send_message(sock, message):
    """
    Кодирование и отправка сообщения
    """
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    logger_g_func.debug(encoded_message)
    sock.send(encoded_message)
