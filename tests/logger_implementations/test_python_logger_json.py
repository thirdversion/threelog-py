import json
import traceback
from typing import Dict, Optional

from assertpy import assert_that
from pytest import LogCaptureFixture, fixture

from strivelogger import StriveLogger
from strivelogger.logger_implementations.python_logger import PythonLogger
from strivelogger.tracer_implementation import TracerImplementation

MOCK_TRACE_ID = "MockTraceId"


class TestTracer(TracerImplementation):
    def get_trace_id(self) -> Optional[str]:
        return MOCK_TRACE_ID


@fixture(autouse=True)
def setup():
    StriveLogger.initialize(PythonLogger(enable_json=True), TestTracer())


def test_message_is_json(caplog: LogCaptureFixture):
    StriveLogger.info("Test message")
    actual = caplog.records[0].message
    record = json.loads(actual)
    assert record


def test_json_contains_extra(caplog: LogCaptureFixture):
    expected_value = "bar"
    extra = {"foo": expected_value}
    StriveLogger.info("", extra=extra)
    actual = caplog.records[0].message
    record: Dict = json.loads(actual)

    assert_that(record.get("extra", None)).is_not_none
    assert_that(record["extra"]["foo"]).is_equal_to(expected_value)


def test_json_contains_trace(caplog: LogCaptureFixture):
    StriveLogger.info("Test message")
    actual = caplog.records[0].message
    record: Dict = json.loads(actual)

    assert_that(record.get("trace_id", None)).is_equal_to(MOCK_TRACE_ID)


def test_json_contains_exception(caplog: LogCaptureFixture):
    expected = ValueError("test error")
    StriveLogger.error("Test message", exc_info=expected)
    record: Dict = json.loads(caplog.records[0].message)
    actual = record.get("exc_info", None)

    assert_that(actual).is_equal_to(traceback.format_exception(expected))


def test_json_contains_error_string(caplog: LogCaptureFixture):
    expected = "some error message"
    StriveLogger.error("Test message", exc_info=expected)
    record: Dict = json.loads(caplog.records[0].message)
    actual = record.get("exc_info", None)

    assert_that(actual).is_equal_to(expected)
