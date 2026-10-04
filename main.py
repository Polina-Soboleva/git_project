import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
app_name = os.getenv("APP_NAME")

errors = []

if not app_name:
    app_name = "git_project"
    print("APP_NAME not set. Using default value: git_project")
else:
    print(f"Application: {app_name}")

if not api_key:
    errors.append("API_KEY is required")

if errors:
    for error in errors:
        print(f"Error: {error}")
    exit(1)

print("API_KEY loaded: True")