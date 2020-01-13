import logging
from misc.constants import LOGGER_NAME, LOG_FORMAT, LOG_PATH

class Logger(object):
    def __init__(self, logger_name, log_path):
        self.logger = logging.getLogger(logger_name)
        hdlr = logging.FileHandler(log_path)
        formatter = logging.Formatter(LOG_FORMAT)
        hdlr.setFormatter(formatter)
        self.logger.addHandler(hdlr) 
        self.logger.setLevel(logging.INFO)

        self.log_init_msg()

    def log_init_msg(self):
        init_msg = "\n\n-------- New run --------\n\n"
        self.log(init_msg)

    def log_end_msg(self):
        end_msg = "\n\n-------- End run  --------\n\n"
        self.log(end_msg)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def log(self, message):
        self.logger.info(message)

logger = Logger(LOGGER_NAME, LOG_PATH)
