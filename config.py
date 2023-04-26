from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "13981526"))
API_HASH = getenv("API_HASH", "5482e90e58d4126b176fcc19d8a33bb8")

BOT_TOKEN = getenv("BOT_TOKEN", "6051801083:AAGqC_FtARwpb5jfepDQx4k8t19AbqYtTh8")
OWNER_ID = int(getenv("OWNER_ID", "5675627801"))

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ffb:ffb@cluster0.ppnwic3.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = getenv("MUST_JOIN", "SOURCELAVA")
