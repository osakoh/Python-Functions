"""
Levels:
DEBUG
INFO

WARNING
ERROR
CRITICAL
"""

import logging

my_format = '%(name)s - %(asctime)s - %(levelname)-8s [%(filename)s:line-%(lineno)d] %(message)s'
logging.basicConfig(format=my_format,
                    level=logging.DEBUG,
                    filename='logs.txt',
                    datefmt='%d/%m/%Y %I:%M:%S')

logger = logging.getLogger('Main Application')

logger.debug('a debug message')
logger.info('an info message')
logger.warning('a warning message')
logger.error('an error message')
logger.critical('a critical message')

logger = logging.getLogger('Main Application.checkout')

logger.debug('a debug message')
logger.info('an info message')
logger.warning('a warning message')
logger.error('an error message')
logger.critical('a critical message')
