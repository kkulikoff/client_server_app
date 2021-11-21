"""
1. Задание на закрепление знаний по модулю CSV.
Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt
и формирующий новый «отчетный» файл в формате CSV. Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными,
их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список.
Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
В этой же функции создать главный список для хранения данных отчета — например,
main_data — и поместить в него названия столбцов отчета в виде списка:
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
"""

import re
from chardet.universaldetector import UniversalDetector
import csv

param = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
file = ['info_1.txt', 'info_2.txt', 'info_3.txt']


def get_data(params, files):
    result_list, main_data, os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], [], [], []
    detector = UniversalDetector()
    for p in params:
        main_data.append(p)
    result_list.append(main_data)
    for doc in files:
        with open(doc, 'rb') as f:
            for line in f:
                detector.feed(line)
                if detector.done:
                    break
            detector.close()
            with open(doc, encoding=detector.result["encoding"]) as f:
                for line in f:
                    if line.find(params[0]) == 0:
                        line = re.split('\s+', line)
                        os_prod_list.append(line[len(line) - 2])
        with open(doc, 'rb') as f:
            for line in f:
                detector.feed(line)
                if detector.done:
                    break
            detector.close()
            with open(doc, encoding=detector.result["encoding"]) as f:
                for line in f:
                    if line.find(params[1]) == 0:
                        line = re.split('\s+', line)
                        os_name_list.append(line[len(line) - 2])
        with open(doc, 'rb') as f:
            for line in f:
                detector.feed(line)
                if detector.done:
                    break
            detector.close()
            with open(doc, encoding=detector.result["encoding"]) as f:
                for line in f:
                    if line.find(params[2]) == 0:
                        line = re.split('\s+', line)
                        os_code_list.append(line[len(line) - 2])
        with open(doc, 'rb') as f:
            for line in f:
                detector.feed(line)
                if detector.done:
                    break
            detector.close()
            with open(doc, encoding=detector.result["encoding"]) as f:
                for line in f:
                    if line.find(params[3]) == 0:
                        line = re.split('\s+', line)
                        os_type_list.append(line[len(line) - 2])
    result_list.append(os_prod_list)
    result_list.append(os_name_list)
    result_list.append(os_code_list)
    result_list.append(os_type_list)
    return result_list


def write_to_csv(params, files):
    with open('list_to_csv.csv', 'w', encoding='utf-8', newline="") as csv_file:
        F_N_WRITER = csv.writer(csv_file)
        F_N_WRITER.writerow(get_data(params, files)[0])
        items = get_data(params, files)[1:]
        count = 0
        while count <= 2:
            F_N_WRITER.writerow([items[0][count]] + [items[1][count]] + [items[2][count]] + [items[3][count]])
            count += 1

# Я понимаю, что решение лютый треш, но задание для меня оказалось весьма сложным.
# Решения я все-равно получил, в сsv файл записывается то, что надо.


write_to_csv(param, file)


