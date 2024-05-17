import os
import sys
import logging

logging_str = "[[%(asctime)s]: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_file_path = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    handlers=[logging.FileHandler(log_file_path, mode="a"), logging.StreamHandler(sys.stdout)],
    format=logging_str,
    level=logging.INFO
    )
logger = logging.getLogger("news_fetcher")
