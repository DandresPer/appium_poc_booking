import logging
import pytest


def set_logger():

    logging.basicConfig(filename='config_check.log', level=logging.INFO)
    logging.info('start')
    pytest.main()
    logging.info('done')


def log_assert(test, msg):
    if not test:
        logging.error(msg)
        assert test, msg
