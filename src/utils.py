import json
from datetime import datetime


def read_json(path):
    """
    Чтение operations.json
    """
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def get_executed_operations(operations):
    """
    Получение только EXECUTED операции
    """
    executed_operations = []
    for operation in operations:
        if operation.get("state") == "EXECUTED":
            executed_operations.append(operation)
    return executed_operations


def sort_operations(operations):
    """
    Сортировка EXECUTED операции по дате убывания
    """
    return sorted(operations, key=lambda operation: operation.get("date"), reverse=True)


def get_last_operations(operations, count):
    """
    Получение среза последних операции
    """
    return operations[:count]


def convert_date(date):
    """
    Конвертирование даты в формат ДД.ММ.ГГ
    """
    datetime_lst = date.split("T")[0]
    data = datetime.strptime(datetime_lst, '%Y-%m-%d').date().strftime('%d.%m.%Y')
    return data


def convert_payment_info(payment):
    """
    Конвертирование счета в формат **1234 или номера карты в формат 1234 56** **** 7890
    """
    if "Счет" in payment:
        return f"{payment[:5]}**{payment[-4:]}"
    else:
        payment_info = payment.split()[len(payment.split()) - 1]
        card_info = payment.replace(payment_info, "")
        payment_info = payment_info[:-10] + "** **** " + payment_info[12:]
        return f'{card_info} {payment_info[:4]} {payment_info[4:]}'

