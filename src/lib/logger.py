import os
import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

file_handler = TimedRotatingFileHandler(
    os.path.join('logs', 'jeeves.log'),
    when='midnight',
    interval=1,
    backupCount=7,
    encoding='utf-8',
    utc=True
)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)