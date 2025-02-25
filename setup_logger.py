import logging


logger = logging.getLogger(__name__)
LOGFORMAT = "%(filename)s: %(lineno)s %(message)s"
logging.basicConfig(format=LOGFORMAT)