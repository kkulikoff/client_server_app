"""Настройки"""
# Порт подключения по умолчанию для сетевого взимодействия
DEFAULT_PORT = 7777
# IP адрес по умолчанию для подключения клиента
DEFAULT_IP_ADDRESS = '127.0.0.1'
# Максимальная очередь подключений. Не обязательно
MAX_CONNECTIONS = 5
# Максимальная длина сообщений в байтах
MAX_PACKAGE_LENGTH = 1024
# Кодировка проекта
ENCODING = 'utf-8'

# Протокол JIM. Основные ключи
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'

# Прочие ключи используемые в протоколе
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'
RESPONSEDEFAULT_IP_ADDRESS = 'responsedefault_ip_address'
