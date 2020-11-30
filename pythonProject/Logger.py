import logging


def log_assert(test, msg):
    if not test:
        logging.error(msg)
        assert test, msg


def error_log(msg):
    logging.error(msg)
