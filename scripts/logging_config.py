"""
File: logging_configpy
Purpose: Demonstrate basic logging configuration in Python
Author: Priya K

Description:
    This script demonstrates how to configure logging in Python.
    It sets up a basic logging configuration to log messages with timestamps.
"""
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')  

logger = logging.getLogger(__name__)

while True:
    try:
        result = 1 / 0
    except ZeroDivisionError:
        logger.error("An error occurred due to division by zero")
    break

if __name__== "__main__":
    logger.info("Print message using logging configuration")
    logger.warning("This is a warning message")    
    logger.debug("This is a debug message")  # This won't be shown because the level is set to INFO
