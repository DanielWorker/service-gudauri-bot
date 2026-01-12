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
APIFY_TOKEN = os.getenv("APIFY_TOKEN")
TEST_MODE = os.getenv("TEST_MODE", "0")

if int(TEST_MODE):
    log_dir = '/Users/spoonsimons/PycharmProjects/service_gudauri_bot/logs'
    path_to_sessions = '/Users/spoonsimons/PycharmProjects/service_gudauri_bot/sessions/'
    path_to_assets = '/Users/spoonsimons/PycharmProjects/service_gudauri_bot/src/assets/'
    paragliding_chat_id = -1001826495601
    notification_box_chat_id = -1001826495601
    food_orders_chat_id = -1001826495601
    massage_chat_id = -1001826495601
    cleaning_chat_id = -1001826495601
    rent_flat_chat_id = -1001826495601
    transfer_chat_id = -1001826495601
else:
    log_dir = '/home/projects/service-gudauri-bot/logs'
    path_to_sessions = '/app/sessions/'
    path_to_assets = '/home/projects/service-gudauri-bot/src/assets/'
    paragliding_chat_id = -1002352593736
    notification_box_chat_id = -1002416931095
    food_orders_chat_id = -1002253195663
    massage_chat_id = -1002269031500
    cleaning_chat_id = -1002322181612
    rent_flat_chat_id = -1002254838245
    transfer_chat_id = -1002658555653


logger = logging.getLogger("telegram")
logger.setLevel(logging.INFO)

log_file_path = os.path.join(log_dir, 'log.log')

# Файловый handler
file_handler = RotatingFileHandler(
    log_file_path,
    maxBytes=200_000,
    backupCount=10,
    encoding='utf-8'
)

formatter = logging.Formatter(
    fmt='%(asctime)s : %(levelname)s : %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)

file_handler.setFormatter(formatter)

# Консольный handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Добавляем оба
logger.addHandler(file_handler)
logger.addHandler(console_handler)

bot = None

dev_bot_user_id = 6193188441
dev_user_id = 365500138

all_service_gudauri_user_id = 7197611297
all_service_gudauri_username = '@AllServiceGudauri'
