"""
Задание на закрепление знаний по модулю json.
Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item),
количество (quantity), цена (price), покупатель (buyer), дата (date).
Функция должна предусматривать запись данных в виде словаря в файл orders.json.
При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""
import datetime
import json

order = {'item': 'camera', 'quantity': 20, 'price': 5600, 'buyer': 'anonymous', 'date': f'{datetime.datetime.now()}'}


def write_order_to_json(**kwargs):
    with open('orders.json') as f:
        data = json.load(f)
    data['orders'].append(kwargs)
    with open('orders.json', 'w') as file:
        json.dump(data, file, indent=4)


write_order_to_json(**order)
