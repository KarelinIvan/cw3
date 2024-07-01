from pathlib import Path

ROOT_PATH = Path(__file__).parent
OPERATIONS_PATH = ROOT_PATH.joinpath("data", "operations.json")
TEST_OPERATIONS_PATH = ROOT_PATH.joinpath("tests", "test_operation.json")

EXECUTED_COUNT = 5
