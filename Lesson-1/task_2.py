"""
Каждое из слов «class», «function», «method»
записать в байтовом типе без преобразования в последовательность кодов
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
"""

WORDS = [b'class', b'function', b'method']


def check_type(arr):
    for word in arr:
        print(f'Тип {arr.index(word) + 1}-го слова: {type(word)}\n'
              f'Содержание {arr.index(word) + 1}-го слова: {word}\n'
              f'Длина {arr.index(word) + 1}-го слова: {len(word)} символов\n')


check_type(WORDS)

# Тип 1-го слова: <class 'bytes'>
# Содержание 1-го слова: b'class'
# Длина 1-го слова: 5 символов
#
# Тип 2-го слова: <class 'bytes'>
# Содержание 2-го слова: b'function'
# Длина 2-го слова: 8 символов
#
# Тип 3-го слова: <class 'bytes'>
# Содержание 3-го слова: b'method'
# Длина 3-го слова: 6 символов