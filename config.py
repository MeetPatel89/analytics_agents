import os
from dotenv import load_dotenv

#load the .env variables
load_dotenv()

ROOT_DIR = os.path.abspath(os.curdir)
API_KEY = os.getenv("OPENAI_API_KEY")