import logging
import os
from datetime import datetime

LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join('logs', LOG_FILE_NAME)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE_NAME)


logging.basicConfig(
    filename=LOG_FILE_PATH, 
    encoding='utf-8', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s %(lineno)s - %(message)s',
    filemode='w'
    )

if __name__ == '__main__':
    logging.info('test')