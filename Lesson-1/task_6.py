from chardet.universaldetector import UniversalDetector
"""
Создать текстовый файл test_file.txt,
заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
strings = ['сетевое программирование', 'сокет', 'декоратор']


def write_in_file(data):
    detector = UniversalDetector()          # подсмотрел на stackoverflow
    with open('test_file.txt', 'w') as f:   # Не указываю явно кодировку
        for d in data:
            f.write(f'{d}\n')
    with open('test_file.txt', 'rb') as f:  # подсмотрел на stackoverflow
        for line in f:                      # подсмотрел на stackoverflow
            detector.feed(line)             # подсмотрел на stackoverflow
            if detector.done:               # подсмотрел на stackoverflow
                break                       # подсмотрел на stackoverflow
        detector.close()                    # подсмотрел на stackoverflow
    print(f'Кодировка: {detector.result["encoding"]}')
    return f'{detector.result["encoding"]}'


def correct_encoding_and_read(filename, newFilename, encoding_from, encoding_to='UTF-8'):
    with open(filename, 'r', encoding=encoding_from) as fr:
        with open(newFilename, 'w', encoding=encoding_to) as fw:
            for line in fr:
                fw.write(line[:-1]+'\r\n')
    with open(newFilename, 'r', encoding='utf-8') as f:  # Указываю явно кодировку
        for line in f:
            print(line)


correct_encoding_and_read('test_file.txt', 'enc_test_file.txt', write_in_file(strings))

# Уверен, что можно сделать всё гораздо проще, но пока бороздил просторы интернета,
# нашел для себя, на данный момент, именно такое решение
