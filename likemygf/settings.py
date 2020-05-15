import os

from dotenv import find_dotenv
from dotenv import load_dotenv

load_dotenv(find_dotenv())

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
CONFIGFILE = os.getenv("CONFIGFILE")
