import os
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
USER_ID = os.getenv("USER_ID")
MAX_INTERVAL= os.getenv("MAX_INTERVAL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")
