import datetime
import logging

import pytz


class Logger:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Logger, cls).__new__(cls)
            cls.__instance.__initialize__logger()
        return cls.__instance

    def __initialize__logger(self):
        self.__logger = logging.getLogger("socialnet")
        if not self.__logger.hasHandlers():
            self.__logger.setLevel(logging.INFO)
            ch = logging.StreamHandler()
            ch.setFormatter(self.CustomFormatter())
            self.__logger.addHandler(ch)

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
        return instance.__logger
