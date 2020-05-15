from typing import List

from pydantic import BaseModel
from pydantic import root_validator


class UserInfo(BaseModel):
    pk: int
    username: str
    is_private: bool

    class Config:
        extra = "ignore"


class FeedItem(BaseModel):
    taken_at: int
    media_id: str
    has_liked: bool
    user: UserInfo

    @root_validator(pre=True)
    def pk_to_media_id(cls, values):
        pk = values.get("pk")
        if "media_id" not in values:
            values["media_id"] = pk
            return values

    class Config:
        extra = "ignore"


class UserFeed(BaseModel):
    items: List[FeedItem]
    num_results: int
    more_available: bool
    next_max_id: str
    auto_load_more_enabled: bool

    class Config:
        extra = "ignore"
