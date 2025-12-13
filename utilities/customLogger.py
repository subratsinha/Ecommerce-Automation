import logging
import os


class LogGen:
    @staticmethod
    def loggen():
        log_dir = os.path.join(os.getcwd(), "Logs")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

        log_file = os.path.join(log_dir, "automation.log")

        logger = logging.getLogger("AutomationLogger")
        logger.setLevel(logging.INFO)

        # If handler already exists, return logger to avoid duplicate handlers
        if any(isinstance(h, logging.FileHandler) and h.baseFilename == os.path.abspath(log_file) for h in logger.handlers):
            return logger

        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        fh = logging.FileHandler(log_file, mode='a', encoding='utf-8')
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        return logger

