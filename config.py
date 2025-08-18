import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

PROTEIN_URL = "https://www.bulk.com/it/products/proteine-del-siero-del-latte-it/bpb-wpc8-0000"
CREATINE_URL = "https://www.bulk.com/it/products/creatine-monohydrate/bpb-cmon-0000"

HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

PRICE_TRESHOLD = {
    'protein':9.99,
    'creatine':4.99
    }

