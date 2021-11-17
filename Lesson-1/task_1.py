"""
Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате 
и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
и также проверить тип и содержимое переменных.
"""
WORDS = ['разработка', 'сокет', 'декоратор']
UNI_WORDS = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
             '\u0441\u043e\u043a\u0435\u0442',
             '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']


def check_type(arr):
    for word in arr:
        print(f'Содержание {arr.index(word) + 1}-го слова: {word}\n'
              f'Тип {arr.index(word) + 1}-го слова: {type(word)}\n')


check_type(WORDS)
check_type(UNI_WORDS)

# Содержание 1-го слова: разработка
# Тип 1-го слова: <class 'str'>
#
# Содержание 2-го слова: сокет
# Тип 2-го слова: <class 'str'>
#
# Содержание 3-го слова: декоратор
# Тип 3-го слова: <class 'str'>
#
# Содержание 1-го слова: разработка
# Тип 1-го слова: <class 'str'>
#
# Содержание 2-го слова: сокет
# Тип 2-го слова: <class 'str'>
#
# Содержание 3-го слова: декоратор
# Тип 3-го слова: <class 'str'>
