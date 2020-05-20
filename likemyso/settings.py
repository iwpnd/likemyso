from typing import List

from dotenv import find_dotenv
from dotenv import load_dotenv
from pydantic import BaseSettings
from pydantic import Field
from pydantic import SecretStr
from pydantic import validator

load_dotenv(find_dotenv())


class Settings(BaseSettings):
    username: str = Field("", env="INSTAGRAM_USERNAME")
    password: SecretStr = Field("", env="INSTAGRAM_PASSWORD")
    file: str = Field("config.json", env="INSTAGRAM_SETTINGSFILE")
    users_to_like: List = Field([], env="INSTAGRAM_USERS_TO_LIKE")
    last_n_pictures: int = Field(5, env="INSTAGRAM_LAST_N_PICTURES")
    time_sleep_between_calls: int = Field(20, env="INSTAGRAM_TIME_SLEEP_BETWEEN_CALLS")

    @validator("file", pre=True, always=True)
    def validate_settingsfile_ending(cls, v, values):
        if not v.endswith(".json"):
            raise ValueError("Settingsfile must be .json")

        return v

    class Config:
        case_sensitive = True

    # class Config:
    # case_sensitive = True
    # fields = {
    # "username": {"env": "INSTAGRAM_USERNAME"},
    # "password": {"env": "INSTAGRAM_PASSWORD"},
    # "file": {"env": "INSTAGRAM_SETTINGSFILE"},
    # "users_to_like": {"env": "INSTAGRAM_USERS_TO_LIKE"},
    # "last_n_pictures": {"env", "INSTAGRAM_LAST_N_PICTURES"},
    # "time_sleep_between_calls": {"env": "INSTAGRAM_TIME_SLEEP_BETWEEN_CALLS"},
    # }
