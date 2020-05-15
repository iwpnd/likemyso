import codecs
import json
from typing import Any
from typing import Dict

from instagram_private_api import Client
from loguru import logger
from pydantic import BaseModel

# https://github.com/ping/instagram_private_api/blob/master/examples/savesettings_logincallback.py


class CacheSettings(BaseModel):
    uuid: str
    device_id: str
    ad_id: str
    session_id: str
    cookie: bytes
    created_ts: int


def to_json(python_object: bytes) -> dict:
    """ Custom serialization for cookie

    Base64 encode cookie before storing the config as settings_file

    Arguments:
            python_object: Python serialized object

    Returns:
            dict
    """
    if isinstance(python_object, bytes):
        return {
            "__class__": "bytes",
            "__value__": codecs.encode(python_object, "base64").decode(),
        }

    raise TypeError(repr(python_object) + " is not JSON serializable")


def from_json(json_object: Dict[str, Any]):
    """ Custom serialization for

    Decode the stored cookie

    Arguments:
            json_object

    Returns:
            json_object
    """

    if "__class__" in json_object and json_object["__class__"] == "bytes":
        return codecs.decode(json_object["__value__"].encode(), "base64")

    return json_object


def onlogin(api: Client, new_settings_file: str) -> None:
    """ Callback function to store Client.settings received upon login to file

    Arguments:
            api (instagram_private_api.Client): Client object after login
            new_settings_file (str): filepath to new settings file

    Returns:
            None
    """
    cache_settings = CacheSettings(**api.settings)

    with open(new_settings_file, "w") as outfile:
        json.dump(cache_settings.dict(), outfile, default=to_json)
        logger.info(f"SAVED: {new_settings_file}")
        logger.debug(f"{cache_settings}")
