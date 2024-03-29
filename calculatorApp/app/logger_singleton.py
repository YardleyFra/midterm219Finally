import logging
import os

class LoggerSingleton:
    _instance = None

    @staticmethod
    def getInstance():
        if LoggerSingleton._instance is None:
            LoggerSingleton()
        return LoggerSingleton._instance

    def __init__(self):
        if LoggerSingleton._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.configure_logging()
            LoggerSingleton._instance = self

    def configure_logging(self):
        log_path = os.path.join(os.path.dirname(__file__), '..', 'info', 'logs.csv')
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s, %(levelname)s, %(message)s',
                            handlers=[logging.FileHandler(log_path), logging.StreamHandler()])
