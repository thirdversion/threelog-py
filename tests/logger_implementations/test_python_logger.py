import logging
from typing import Optional

from assertpy import assert_that
from pytest import LogCaptureFixture, fixture

from threelog import ThreeLog
from threelog.logger_implementations.python_logger import PythonLogger
from threelog.tracer_implementation import TracerImplementation

MOCK_TRACE_ID = "MockTraceId"


class TestTracer(TracerImplementation):
    def get_trace_id(self) -> Optional[str]:
        return MOCK_TRACE_ID


@fixture(autouse=True)
def setup():
    ThreeLog.initialize(PythonLogger(), TestTracer())


def test_can_log_debug(caplog: LogCaptureFixture):
    expected = "Test message"
    with caplog.at_level(logging.DEBUG):
        ThreeLog.debug(expected)
    actual = caplog.text

    assert_that(actual).contains("DEBUG")
    assert_that(actual).contains(expected)
    assert_that(actual).contains(MOCK_TRACE_ID)


def test_can_log_debug_extra(caplog: LogCaptureFixture):
    expected = {"foo": "bar"}
    with caplog.at_level(logging.DEBUG):
        ThreeLog.debug("", extra=expected)
    actual = caplog.text

    assert_that(actual).contains("DEBUG")
    assert_that(actual).contains(str(expected))


def test_can_log_info(caplog: LogCaptureFixture):
    expected = "Test message"
    ThreeLog.info(expected)
    actual = caplog.text

    assert_that(actual).contains("INFO")
    assert_that(actual).contains(expected)
    assert_that(actual).contains(MOCK_TRACE_ID)


def test_can_log_info_extra(caplog: LogCaptureFixture):
    expected = {"foo": "bar"}
    ThreeLog.info("", extra=expected)
    actual = caplog.text

    assert_that(actual).contains("INFO")
    assert_that(actual).contains(str(expected))


def test_can_log_warn(caplog: LogCaptureFixture):
    expected = "Test message"
    ThreeLog.warn(expected)
    actual = caplog.text

    assert_that(actual).contains("WARN")
    assert_that(actual).contains(expected)
    assert_that(actual).contains(MOCK_TRACE_ID)


def test_can_log_warn_extra(caplog: LogCaptureFixture):
    expected = {"foo": "bar"}
    ThreeLog.warn("", extra=expected)
    actual = caplog.text

    assert_that(actual).contains("WARN")
    assert_that(actual).contains(str(expected))


def test_can_log_error(caplog: LogCaptureFixture):
    expected = "Test message"
    ThreeLog.error(expected)
    actual = caplog.text

    assert_that(actual).contains("ERROR")
    assert_that(actual).contains(expected)
    assert_that(actual).contains(MOCK_TRACE_ID)


def test_can_log_error_extra(caplog: LogCaptureFixture):
    expected = {"foo": "bar"}
    ThreeLog.error("", extra=expected)
    actual = caplog.text

    assert_that(actual).contains("ERROR")
    assert_that(actual).contains(str(expected))


def test_can_log_error_exception(caplog: LogCaptureFixture):
    expected = ValueError("test error")
    ThreeLog.error("", exc_info=expected)
    actual = caplog.text

    assert_that(actual).contains("ERROR")
    assert_that(actual).contains(str(expected))
