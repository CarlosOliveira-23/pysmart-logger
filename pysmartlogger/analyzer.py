import re


class LogAnalyzer:
    ERROR_PATTERNS = {
        "ConnectionError": "Check your internet connection or firewall.",
        "TimeoutError": "The connection timed out. Try increasing the timeout.",
        "PermissionError": "You do not have permission to access this resource.",
        "FileNotFoundError": "The specified file was not found.",
        "ValueError": "There was a value error in the data processed."
    }

    @staticmethod
    def analyze_log(log_message):
        for error, suggestion in LogAnalyzer.ERROR_PATTERNS.items():
            if re.search(error, log_message, re.IGNORECASE):
                return f"🛠 Suggestion: {suggestion}"
        return "No suggestions available"


if __name__ == "__main__":
    log_msg = "TimeoutError: Response time has expired"
    print(LogAnalyzer.analyze_log(log_msg))
