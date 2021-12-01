# logging - стандартный модуль для организации логирования
import logging
# Можно выполнить более расширенную настройку логирования.

# Создаем объекты-логгеры:
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('app.server')
logger_gf = logging.getLogger('app.g_func')

# Создаем объект форматирования:
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s ")
formatter_g_func = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s ")

# Создаем файловый обработчик логирования (можно задать кодировку):
fh = logging.FileHandler("log/server.log", encoding='utf-8')
handler = RotatingFileHandler('log/server_01.log', maxBytes=2000, backupCount=10)
logger.addHandler(handler)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

# Создаем файловый обработчик логирования для функций клиента и сервера general_func
fh_func = logging.FileHandler('log/general_func.log', encoding='utf-8')
fh_func.setLevel(logging.DEBUG)
fh_func.setFormatter(formatter_g_func)

# Добавляем в логгер новый обработчик событий и устанавливаем уровень логирования
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

logger_gf.addHandler(fh_func)
logger_gf.setLevel(logging.DEBUG)

# if __name__ == '__main__':
#     # Создаем потоковый обработчик логирования (по умолчанию sys.stderr):
#     console = logging.StreamHandler()
#     console.setLevel(logging.DEBUG)
#     console.setFormatter(formatter)
#     logger.addHandler(console)
#     logger.info('Тестовый запуск логирования')