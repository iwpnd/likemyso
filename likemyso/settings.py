from typing import List

from dotenv import find_dotenv
from dotenv import load_dotenv
from pydantic import BaseSettings
from pydantic import SecretStr
from pydantic import validator

load_dotenv(find_dotenv())


class Credentials(BaseSettings):
    username: str
    password: SecretStr

    class Config:
        case_sensitive = False
        env_prefix = "INSTAGRAM_"


class Settings(BaseSettings):
    settings_file: str = "config.json"
    users_to_like: List = []
    last_n_pictures: int = 5
    time_sleep_between_calls: int = 20

    @validator("settings_file", pre=True, always=True)
    def validate_settingsfile_ending(cls, v, values):
        if not v.endswith(".json"):
            raise ValueError("Settings_file must be .json")

        return v

    class Config:
        env_prefix = "INSTAGRAM_"
        case_sensitive = False
