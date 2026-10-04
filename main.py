import os
from dotenv import load_dotenv

load_dotenv()  # reads the .env file in the project root

database_url = os.getenv("DATABASE_URL")
api_key = os.getenv("OPENAI_API_KEY")

print("Connecting to:", database_url)