# from src.logger import configure_logger
# import logging

# # initialize your logger
# configure_logger()

# logging.debug("This is a debug message.")
# logging.info("This is an info message.")
# logging.warning("This is a warning message.")
# logging.error("This is an error message.")
# logging.critical("This is a critical message.")

from src.logger import logging
from src.exception import MyException
import sys

try:
    a = 1 + 'Z'
except Exception as e:
    logging.error("Exception occurred", exc_info=True)
    raise MyException(e, sys)
