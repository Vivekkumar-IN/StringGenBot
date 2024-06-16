from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

OWNER_ID = getenv("OWNER_ID", 1356469075)
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/FallenAssociation")
