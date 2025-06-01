# config.py

from os import getenv
from dotenv import load_dotenv

load_dotenv()  # .env file load kar raha hai

INST_COOKIES = getenv("INSTA_COOKIES", "")
YTUB_COOKIES = getenv("YT_COOKIES", "")

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
MONGO_DB = getenv("MONGO_DB")
LOG_GROUP = getenv("LOG_GROUP")
CHANNEL_ID = int(getenv("CHANNEL_ID"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", 999999))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", 999999))
WEBSITE_URL = getenv("WEBSITE_URL")
AD_API = getenv("AD_API", "")
STRING = getenv("STRING")
DEFAULT_SESSION = getenv("DEFAUL_SESSION")
