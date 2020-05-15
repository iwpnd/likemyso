from typing import List

from pydantic import BaseModel
from pydantic import root_validator


class Picture(BaseModel):
    taken_at: int
    media_id: str
    has_liked: bool

    @root_validator(pre=True)
    def pk_to_media_id(cls, values):
        # pk == media_id yet media_id is only used in caption
        id = values.get("id")
        if "media_id" not in values:
            values["media_id"] = id
            return values

    class Config:
        extra = "ignore"


class UserFeed(BaseModel):
    items: List[Picture]
    num_results: int

    class Config:
        extra = "ignore"


class User(BaseModel):
    username: str
    latest_feed: UserFeed
