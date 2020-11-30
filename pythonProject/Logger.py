import logging


def set_logger():
    logging.basicConfig(filename='config_check_7.log', level=logging.NOTSET)


def log_assert(test, msg):
    if not test:
        logging.error(msg)
        assert test, msg


def error_log(msg):
    logging.error(msg)
