from typing import Optional

from assertpy import assert_that
from pytest import CaptureFixture, fixture

from strivelogger import StriveLogger
from strivelogger.logger_implementations.console_logger import ConsoleLogger
from strivelogger.tracer_implementation import TracerImplementation

MOCK_TRACE_ID = "MockTraceId"


class TestTracer(TracerImplementation):
    def get_trace_id(self) -> Optional[str]:
        return MOCK_TRACE_ID


@fixture(autouse=True)
def setup():
    StriveLogger.initialize(ConsoleLogger(), TestTracer())


def test_can_log_debug(capfd: CaptureFixture[str]):
    expected = "Test message"
    StriveLogger.debug(expected)
    actual, err = capfd.readouterr()
    assert_that(actual).contains("DEBUG:")
    assert_that(actual).contains(expected)
    assert_that(actual).contains(MOCK_TRACE_ID)


def test_can_log_debug_extra(capfd: CaptureFixture[str]):
    expected = {"foo": "bar"}
    StriveLogger.debug("", extra=expected)
    actual, _ = capfd.readouterr()
    assert_that(actual).contains("DEBUG:")
    assert_that(actual).contains(str(expected))


def test_can_log_info(capfd: CaptureFixture[str]):
    expected = "Test message"
    StriveLogger.info(expected)
    actual, _ = capfd.readouterr()
    assert_that(actual).contains("INFO:")
    assert_that(actual).contains(expected)
    assert_that(actual).contains(MOCK_TRACE_ID)


def test_can_log_info_extra(capfd: CaptureFixture[str]):
    expected = {"foo": "bar"}
    StriveLogger.info("", extra=expected)
    actual, _ = capfd.readouterr()
    assert_that(actual).contains("INFO:")
    assert_that(actual).contains(str(expected))


def test_can_log_warn(capfd: CaptureFixture[str]):
    expected = "Test message"
    StriveLogger.warn(expected)
    actual, _ = capfd.readouterr()
    assert_that(actual).contains("WARN:")
    assert_that(actual).contains(expected)
    assert_that(actual).contains(MOCK_TRACE_ID)


def test_can_log_warn_extra(capfd: CaptureFixture[str]):
    expected = {"foo": "bar"}
    StriveLogger.warn("", extra=expected)
    actual, _ = capfd.readouterr()
    assert_that(actual).contains("WARN:")
    assert_that(actual).contains(str(expected))


def test_can_log_error(capfd: CaptureFixture[str]):
    expected = "Test message"
    StriveLogger.error(expected)
    actual, _ = capfd.readouterr()
    assert_that(actual).contains("ERROR:")
    assert_that(actual).contains(expected)
    assert_that(actual).contains(MOCK_TRACE_ID)


def test_can_log_error_extra(capfd: CaptureFixture[str]):
    expected = {"foo": "bar"}
    StriveLogger.error("", extra=expected)
    actual, _ = capfd.readouterr()
    assert_that(actual).contains("ERROR:")
    assert_that(actual).contains(str(expected))


def test_can_log_error_exception(capfd: CaptureFixture[str]):
    expected = ValueError("test error")
    StriveLogger.error("", exc_info=expected)
    actual, _ = capfd.readouterr()
    assert_that(actual).contains("ERROR:")
    assert_that(actual).contains(str(expected))
