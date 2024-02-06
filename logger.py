print("hi i am rajesh")

import logging
logging.basicConfig(filename="text.log",level=logging.INFO)
logging.info("this is my first logging information")
logging.error("this is my error")
logging.critical("this is my critical message")
logging.warning("this is my warning")
logging.debug("ths is my related to debug") # it wont show any thing because you set level=logging.INFO
logging.shutdown()

import logging
logging.basicConfig(filename="test1.log",level=logging.DEBUG,format="%(asctime)s %(message)s")
logging.info("this is my debug file")
logging.error("this is my debug error file")
logging.warning("this is my warning file")
logging.debug("this my debug file")
logging.shutdown()

import logging
logging.basicConfig(filename="test2.log",level=logging.CRITICAL,format="%(asctime)s %(message)s")
logging.info("this is my critical file")


