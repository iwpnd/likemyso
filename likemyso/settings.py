import os

from dotenv import find_dotenv
from dotenv import load_dotenv

load_dotenv(find_dotenv())

INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME", "default")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD", "default")
SETTINGSFILE = os.getenv("SETTINGSFILE", "config.json")
USERS_TO_LIKE = os.getenv("USERS_TO_LIKE", "").split(",")
LAST_N_PICTURES = int(os.getenv("LAST_N_PICTURES", 5))
TIME_SLEEP_BETWEEN_CALLS = int(os.getenv("TIME_SLEEP_BETWEEN_CALLS", 10))
