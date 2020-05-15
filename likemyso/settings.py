import os

from dotenv import find_dotenv
from dotenv import load_dotenv

load_dotenv(find_dotenv())

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
CONFIGFILE = os.getenv("CONFIGFILE")
USERS_TO_LIKE = [i for i in os.environ.get("USERS_TO_LIKE").split(",")]
