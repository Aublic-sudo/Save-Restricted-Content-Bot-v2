# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "25352517"))
API_HASH = getenv("API_HASH", "2b7e6cf7752c3af91f958d67793a3e0b")
BOT_TOKEN = getenv("BOT_TOKEN", "8025159606:AAGXRIe53L3jj9vS0-wtGEy_pTq7p_Yd1pc")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7360968885").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://rstock937:45674567uUu@cluster0.hte7t.mongodb.net/
")
LOG_GROUP = getenv("LOG_GROUP", "-1002659745442")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002698150766"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "999999"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "999999"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
