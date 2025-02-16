from pysmartlogger.logger import PySmartLogger
from pysmartlogger.analyzer import LogAnalyzer
from pysmartlogger.notifier import Notifier

logger = PySmartLogger()

log_message = "TimeoutError: Response time has expired"
logger.log(log_message, "error")

suggestion = LogAnalyzer.analyze_log(log_message)
logger.log(suggestion, "info")

telegram_token = "YOU_TOKEN"
telegram_chat_id = "YOU_CHAT_ID"
Notifier.send_telegram_alert(telegram_token, telegram_chat_id, "🚨 Critical system error!")
