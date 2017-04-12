# myLogger.py
import logging


def write(log_level, msg):
    logging.basicConfig(format='%(asctime)s(%(levelname)s) %(message)s',
                        datefmt='[%Y-%m-%dT%H:%M:%S]',
                        filename='example.log', level=logging.DEBUG)
    log_level(msg)
