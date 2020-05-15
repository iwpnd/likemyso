import codecs
import json
from typing import Any
from typing import Dict

from instagram_private_api import Client
from loguru import logger

# https://github.com/ping/instagram_private_api/blob/master/examples/savesettings_logincallback.py


def to_json(python_object: Dict[str, Any]) -> dict:
    if isinstance(python_object, bytes):
        return {
            "__class__": "bytes",
            "__value__": codecs.encode(python_object, "base64").decode(),
        }
    raise TypeError(repr(python_object) + " is not JSON serializable")


def from_json(json_object: Dict[str, Any]):
    if "__class__" in json_object and json_object["__class__"] == "bytes":
        return codecs.decode(json_object["__value__"].encode(), "base64")

    return json_object


def onlogin_callback(api: Client, new_settings_file: str) -> None:
    cache_settings = api.settings

    with open(new_settings_file, "w") as outfile:
        json.dump(cache_settings, outfile, default=to_json)
        logger.info(f"SAVED: {new_settings_file}")
