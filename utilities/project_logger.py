import logging
import os
import time
from datetime import datetime

from utilities.read_run_settings import ReadConfig

logger = logging.getLogger(__name__)


def _set_logger_level():
    logging_level = ReadConfig.get_logging_level()
    if logging_level == "CRITICAL":
        return 50
    elif logging_level == "ERROR":
        return 40
    elif logging_level == "WARNING":
        return 30
    elif logging_level == "DEBUG":
        return 10
    else:
        return 20


def set_logger():
    logger.setLevel(_set_logger_level())
    formatter = logging.Formatter('%(asctime)s:%(pathname)s:%(funcName)s:%(lineno)d:%(message)s')
    abs_path = os.path.abspath(r"..\..\logs")
    file_handler = logging.FileHandler(
        f'{abs_path}\\{datetime.fromtimestamp(time.time()).strftime("%Y%m%d_%H%M%S")}.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    stream_handler = logging.StreamHandler()
    logger.addHandler(stream_handler)
