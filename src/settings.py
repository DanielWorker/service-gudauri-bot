import logging
from logging.handlers import RotatingFileHandler

from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_API_ID = os.getenv("BOT_API_ID")
BOT_API_HASH = os.getenv("BOT_API_HASH")
BOT_ID = os.getenv("BOT_ID")
BOT_USERNAME = os.getenv("BOT_USERNAME")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TEST_MODE = os.getenv("TEST_MODE")

if int(TEST_MODE):
    log_dir = '/Users/spoonsimons/PycharmProjects/service_gudauri_bot/logs'
    path_to_sessions = '/Users/spoonsimons/PycharmProjects/service_gudauri_bot/sessions/'
else:
    log_dir = '/home/service-gudauri-bot/logs'
    path_to_sessions = '/home/service-gudauri-bot/sessions/'


logger = logging.getLogger("telegram")
logger.setLevel(logging.INFO)

log_file_path = os.path.join(log_dir, 'log.log')

if not os.path.isfile(log_file_path):
    with open(log_file_path, 'w'):
        pass

handler = RotatingFileHandler(log_file_path, maxBytes=200000, backupCount=10, encoding='utf-8')
formatter = logging.Formatter(fmt='%(asctime)s : %(levelname)s : %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

handler.setFormatter(formatter)
logger.addHandler(handler)

bot = None

dev_bot_user_id = 6193188441
dev_user_id = 365500138

all_service_gudauri_user_id = 7197611297
all_service_gudauri_username = '@AllServiceGudauri'

notification_box_chat_id = -1002416931095  # -1001826495601


