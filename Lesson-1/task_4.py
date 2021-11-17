"""
Преобразовать слова «разработка», «администрирование», «protocol», «standard»
из строкового представления в байтовое и выполнить обратное преобразование
(используя методы encode и decode).
"""
WORDS = ['разработка', 'администрирование', 'protocol', 'standard']


def magic_type(arr):
    for word in arr:
        print(f'Содержимое: {word}, тип: {type(word)}')    # исходные данные
        word = word.encode('utf-8')                        # преобразование в байты
        print(f'Содержимое: {word}, тип: {type(word)}')    # вывод данных в байтах
        word = word.decode('utf-8')                        # обратное преобразование
        print(f'Содержимое: {word}, тип: {type(word)}\n')  # вывод данных в str


magic_type(WORDS)

# Содержимое: разработка, тип: <class 'str'>
# Содержимое: b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0', тип: <class 'bytes'>
# Содержимое: разработка, тип: <class 'str'>
#
# Содержимое: администрирование, тип: <class 'str'> Содержимое:
# b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0
# \xd0\xbd\xd0\xb8\xd0\xb5', тип: <class 'bytes'> Содержимое: администрирование, тип: <class 'str'>
#
# Содержимое: protocol, тип: <class 'str'>
# Содержимое: b'protocol', тип: <class 'bytes'>
# Содержимое: protocol, тип: <class 'str'>
#
# Содержимое: standard, тип: <class 'str'>
# Содержимое: b'standard', тип: <class 'bytes'>
# Содержимое: standard, тип: <class 'str'>
