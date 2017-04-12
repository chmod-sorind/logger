# myLyb.py
import myLogger
import logging
import time


def do_something():
    i = 0
    myLogger.write(logging.info, "Countdown started.")
    while i < 10:
        try:
            myLogger.write(logging.debug, i)
            i += 1
            time.sleep(1)
        except Exception as e:
            myLogger.write(logging.warn, e)
            print(e)
    myLogger.write(logging.info, "Countdown stopped!")

do_something()
