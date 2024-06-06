import datetime
import logging

import pytz


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.__initialize_logger()
        return cls._instance

    def __initialize_logger(self):
        self._logger = logging.getLogger("socialnet")
        if not self._logger.hasHandlers():
            self._logger.setLevel(logging.INFO)
            ch = logging.StreamHandler()
            ch.setFormatter(self.CustomFormatter())
            self._logger.addHandler(ch)

    class CustomFormatter(logging.Formatter):
        def format(self, record):
            lisbon_tz = pytz.timezone("Europe/Lisbon")
            timestamp = datetime.datetime.now(lisbon_tz).strftime(
                "%Y-%m-%d %H:%M:%S %Z"
            )
            return f"[{record.levelname}] [{timestamp}] {record.getMessage()}"

    @staticmethod
    def get_logger():
        instance = Logger()
        return instance._logger
