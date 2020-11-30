import logging
import pytest


def set_logger():
    logging.basicConfig(filename='config_check_7.log', level=logging.NOTSET)
    logging.info('start')
    pytest.main()
    logging.info('done')


def log_assert(test, msg):
    if not test:
        logging.error(msg)
        assert test, msg
