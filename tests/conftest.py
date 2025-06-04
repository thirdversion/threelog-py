import pytest

from threelog.three_logger import ThreeLog


@pytest.fixture(autouse=True)
def reset_logger():
    ThreeLog.reset()
