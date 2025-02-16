import os
import pytest
from pysmartlogger.logger import PySmartLogger
from pysmartlogger.analyzer import LogAnalyzer
from pysmartlogger.utils import Utils


@pytest.fixture
def logger():
    return PySmartLogger(log_file="test_logs.txt")


def test_logger_info(logger):
    """Tests whether the logger correctly writes an INFO log"""
    logger.log("Teste de log INFO", "info")
    with open("test_logs.txt", "r", encoding="utf-8") as f:
        logs = f.read()
    assert "Teste de log INFO" in logs


def test_log_analysis():
    """Tests whether log analysis returns suggestions correctly"""
    error_message = "TimeoutError: Response time has expired"
    suggestion = LogAnalyzer.analyze_log(error_message)
    assert "Suggestion" in suggestion


def test_log_filename():
    """Tests whether the generated log file name is in the correct format"""
    filename = Utils.get_log_filename()
    assert filename.startswith("logs_") and filename.endswith(".txt")


if __name__ == "__main__":
    pytest.main()
