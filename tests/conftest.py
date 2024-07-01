import pytest


@pytest.fixture
def executed_operations_fixture():
    operations = [
        {
            "id": 414894334,
            "state": "EXECUTED",
            "date": "2019-06-30T15:11:53.136004",
            "operationAmount": {
                "amount": "95860.47",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 59956820797131895975",
            "to": "Счет 43475624104328495820"
        },
        {
            "id": 414894334,
            "state": "EXECUTED",
            "date": "2019-06-30T15:11:53.136004",
            "operationAmount": {
                "amount": "95860.47",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 59956820797131895975",
            "to": "Счет 43475624104328495820"
        },
    ]
    return operations


@pytest.fixture
def canceled_operations_fixture():
    operations = [
        {
            "id": 414894334,
            "state": "CANCELED",
            "date": "2019-06-30T15:11:53.136004",
            "operationAmount": {
                "amount": "95860.47",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 59956820797131895975",
            "to": "Счет 43475624104328495820"
        },
        {
            "id": 414894334,
            "state": "CANCELED",
            "date": "2019-06-30T15:11:53.136004",
            "operationAmount": {
                "amount": "95860.47",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 59956820797131895975",
            "to": "Счет 43475624104328495820"
        },
    ]
    return operations


@pytest.fixture
def operations_fixture():
    operations = [
        {
            "id": 414894334,
            "state": "EXECUTED",
            "date": "2019-06-30T15:11:53.136004",
            "operationAmount": {
                "amount": "95860.47",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 59956820797131895975",
            "to": "Счет 43475624104328495820"
        },
        {
            "id": 414894334,
            "state": "CANCELED",
            "date": "2020-06-30T15:11:53.136004",
            "operationAmount": {
                "amount": "95860.47",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 59956820797131895975",
            "to": "Счет 43475624104328495820"
        },
    ]
    return operations
