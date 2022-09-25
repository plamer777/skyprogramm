import logging
from config.config import LOG_FORMAT


def get_new_logger(filename, name='api_logger', format_str=LOG_FORMAT):

    logger = logging.getLogger(name)
    handler = logging.FileHandler(filename=filename, encoding='utf-8')
    formatter = logging.Formatter(format_str)

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    return logger
