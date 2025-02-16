import logging
import datetime
import os


class PySmartLogger:
    def __init__(self, log_file="logs.txt"):
        self.logger = logging.getLogger("PySmartLogger")
        self.logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        log_format = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(log_format)
        console_handler.setFormatter(log_format)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def log(self, message, level="info"):
        if level.lower() == "info":
            self.logger.info(message)
        elif level.lower() == "debug":
            self.logger.debug(message)
        elif level.lower() == "error":
            self.logger.error(message)
        elif level.lower() == "warning":
            self.logger.warning(message)
        elif level.lower() == "critical":
            self.logger.critical(message)
        else:
            self.logger.info(message)


if __name__ == "__main__":
    logger = PySmartLogger()
    logger.log("System started", "info")
    logger.log("Debugging enabled", "debug")
    logger.log("Error found!", "error")
