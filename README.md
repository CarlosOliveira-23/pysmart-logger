# PySmartLogger

## 🚀 Intelligent Logging System for Python

**PySmartLogger** is an advanced logging system that goes beyond simple log recording. It includes **AI-powered log analysis**, **pattern detection**, and **real-time notifications** via Telegram and Discord.

### 🔥 Features
- 📜 **Advanced Logging**: Register logs with different levels (INFO, DEBUG, ERROR, etc.).
- 🧠 **AI-Based Log Analysis**: Detects error patterns and suggests solutions.
- 📊 **Log Grouping**: Reduces redundancy by merging similar logs.
- 🔔 **Real-Time Notifications**: Sends alerts to Telegram and Discord.
- 📂 **Log File Management**: Automatically deletes old logs to save space.
- 📡 **Easy API Integration**: Works with any Python application.

---

## 📌 Installation

Install the package using pip:

```bash
pip install pysmartlogger
```

Or install from source:

```bash
git clone https://github.com/yourusername/pysmartlogger.git
cd pysmartlogger
pip install .
```

---

## 🚀 Getting Started

### 1️⃣ Basic Usage

```python
from pysmartlogger.logger import PySmartLogger

logger = PySmartLogger()
logger.log("Application started", "info")
logger.log("Debug mode enabled", "debug")
logger.log("Error detected!", "error")
```

### 2️⃣ Log Analysis

```python
from pysmartlogger.analyzer import LogAnalyzer

log_message = "TimeoutError: The response time expired"
suggestion = LogAnalyzer.analyze_log(log_message)
print(suggestion)  # 🛠 Suggestion: Try increasing the timeout limit.
```

### 3️⃣ Sending Alerts to Telegram and Discord

```python
from pysmartlogger.notifier import Notifier

telegram_token = "YOUR_TELEGRAM_BOT_TOKEN"
telegram_chat_id = "YOUR_CHAT_ID"
discord_webhook = "YOUR_DISCORD_WEBHOOK_URL"

Notifier.send_telegram_alert(telegram_token, telegram_chat_id, "🚨 Critical error detected!")
Notifier.send_discord_alert(discord_webhook, "🚨 Critical error detected!")
```

---

## ⚙️ Configuration

You can customize logging settings by modifying `logger.py`.  
To change the **log storage path**, edit:

```python
log_file = "logs/system_logs.txt"
```

To change the **notification settings**, update:

```python
TELEGRAM_TOKEN = "your-telegram-bot-token"
TELEGRAM_CHAT_ID = "your-chat-id"
DISCORD_WEBHOOK_URL = "your-discord-webhook-url"
```

---

## 🧪 Running Tests

To test the library, install `pytest`:

```bash
pip install pytest
```

Then run the tests:

```bash
pytest tests/test_logger.py
```

---

## 📜 License

PySmartLogger is released under the **MIT License**.

---

## 📞 Contact

For support, feature requests, or contributions, contact:

- **Author**: Your Name
- **Email**: your.email@example.com
- **GitHub**: [yourusername](https://github.com/yourusername)
