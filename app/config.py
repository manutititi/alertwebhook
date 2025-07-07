import os

class Settings:
    TIMEZONE = os.getenv("TZ", "Europe/Madrid")
    LOG_DIR = os.getenv("LOG_DIR", "logs")
    LOG_FILE = os.path.join(LOG_DIR, "alertmanager_webhook.log")
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

settings = Settings()
