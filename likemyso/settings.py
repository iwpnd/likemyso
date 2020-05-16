import os

from dotenv import find_dotenv
from dotenv import load_dotenv

load_dotenv(find_dotenv())

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
SETTINGSFILE = os.getenv("SETTINGSFILE")
USERS_TO_LIKE = [i for i in os.environ.get("USERS_TO_LIKE").split(",")]
LAST_N_PICTURES = int(os.getenv("LAST_N_PICTURES"))
TIME_SLEEP_BETWEEN_CALLS = int(os.getenv("TIME_SLEEP_BETWEEN_CALLS"))
