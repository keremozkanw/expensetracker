import os
from dotenv import load_dotenv

# .env dosyasını yükleyelim
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://username:bebis123@localhost/expense_tracker")