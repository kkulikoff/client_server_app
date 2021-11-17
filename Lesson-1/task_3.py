"""
Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе.
"""
WORDS = [b'attribute', b'класс', b'функция', b'type']

print(WORDS)

#     WORDS = [b'attribute', b'класс', b'функция', b'type']
#                           ^
# SyntaxError: bytes can only contain ASCII literal characters.
#
# Таким образом в тип данных 'bytes' нельзя вписывать кириллицу,
# иначе произойдет синтаксическая ошибка и код не выполнится.
#
# Ответ: «класс», «функция»
