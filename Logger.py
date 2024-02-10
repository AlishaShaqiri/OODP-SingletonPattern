import logging
import os

class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
            cls._instance.initialize_logger()
        return cls._instance

    def initialize_logger(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        log_file = os.path.join(os.getcwd(), 'application.log')

        # Ensure log directory exists
        log_dir = os.path.dirname(log_file)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def log(self, message):
        self.logger.info(message)


# Example usage:
if __name__ == "__main__":
    logger1 = Logger()
    logger1.log("This is a log message from logger1")

    logger2 = Logger()
    logger2.log("This is a log message from logger2")
