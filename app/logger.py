import os
import logging
from logging.handlers import RotatingFileHandler
from app.config import settings

os.makedirs(settings.LOG_DIR, exist_ok=True)

logger = logging.getLogger("webhook_logger")
logger.setLevel(logging.INFO)

handler = RotatingFileHandler(settings.LOG_FILE, maxBytes=1_000_000, backupCount=5)
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
