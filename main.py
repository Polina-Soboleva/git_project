import os
from dotenv import load_dotenv

load_dotenv()

app_name = os.getenv("APP_NAME")
api_key = os.getenv("API_KEY")

if not app_name and not api_key:
    print("Error: APP_NAME and API_KEY environment variables are not set.")
    exit(1)

if not app_name:
    print("Error: APP_NAME environment variable is not set.")
    exit(1)

if not api_key:
    print("Error: API_KEY environment variable is not set.")
    exit(1)

print(f"Application: {app_name}")
print(f"API_KEY loaded: True")