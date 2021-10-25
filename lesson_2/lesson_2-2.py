"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
a. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item),
количество (quantity), цена (price), покупатель (buyer), дата (date).
Функция должна предусматривать запись данных в виде словаря в файл orders.json.
При записи данных указать величину отступа в 4 пробельных символа;

b. Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""

import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json') as f_n:
        f_n_content = f_n.read()
        obj = json.loads(f_n_content)
    if obj and 'orders' in obj.keys():
        old_orders = obj['orders']
    else:
        old_orders = []
    new_order = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }
    old_orders.append(new_order)
    dict_to_json = {'orders': old_orders}
    with open('orders.json', 'w') as f_n:
        f_n.write(json.dumps(dict_to_json, indent=4))


if __name__ == '__main__':
    write_order_to_json('54767', 2, 1200, 'Лукреция', '2021-08-15')
    write_order_to_json('48962', 3, 4000, 'Самуэль', '2021-09-16')
    write_order_to_json('35893', 1, 2500, 'Пабло', '2021-10-17')
    write_order_to_json('25489', 4, 1300, 'Эстер', '2021-11-18')
