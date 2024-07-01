from config import TEST_OPERATIONS_PATH
from src.utils import (get_executed_operations, sort_operations, get_last_operations, convert_date,
                       convert_payment_info, read_json)


def test_read_json():
    operation = read_json(TEST_OPERATIONS_PATH)
    assert len(operation) == 3


def test_get_executed_operations(executed_operations_fixture, canceled_operations_fixture, operations_fixture):
    operation = get_executed_operations(executed_operations_fixture)
    assert len(operation) == 2
    operation = get_executed_operations(canceled_operations_fixture)
    assert len(operation) == 0
    operation = get_executed_operations(operations_fixture)
    assert len(operation) == 1


def test_sort_operations(operations_fixture):
    operation = sort_operations(operations_fixture)
    assert operation[0].get("date") == "2020-06-30T15:11:53.136004"
    assert operation[0].get("date") > operation[1].get("date")


def test_get_last_operations(executed_operations_fixture, canceled_operations_fixture):
    operation = get_last_operations(executed_operations_fixture, count=1)
    assert operation
    operation = get_last_operations(canceled_operations_fixture, count=4)
    assert operation


def test_convert_date():
    operation = convert_date(date="2019-06-30T15:11:53.136004")
    assert operation == "30.06.2019"
    operation = convert_date(date="2020-06-30T15:11:53.136004")
    assert operation == "30.06.2020"


def test_convert_payment_info():
    operation = convert_payment_info(payment="Счет 59956820797131895975")
    assert operation == "Счет **5975"
    operation = convert_payment_info(payment="Счет 43475624104328495820")
    assert operation == "Счет **5820"
