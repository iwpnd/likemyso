import json
import os.path

from instagram_private_api import __version__ as client_version
from instagram_private_api import Client
from instagram_private_api import ClientCookieExpiredError
from instagram_private_api import ClientError
from instagram_private_api import ClientLoginError
from instagram_private_api import ClientLoginRequiredError
from loguru import logger

from likemygf import callback
from likemygf import settings


def login() -> Client:
    """ Authenticate with instagram API and prevent re-login if possible
    see: https://instagram-private-api.readthedocs.io/en/latest/usage.html#avoiding-re-login

    1. check if old settings can be found at settings.SETTINGFILE

    if yes:
        use old settings and cookies
            if is_expired: log back in with device_id and store to settings.SETTINGFILE

    if no:
        login with settings.USERNAME, settings.PASSWORD and store to settings.SETTINGFILE


    Returns:
            Client
    """

    logger.info(f"Client version: {client_version}")
    device_id = None

    try:
        settings_file = settings.SETTINGFILE

        if not os.path.isfile(settings_file):
            logger.error(f"Unable to find file: {settings_file}")

            api = Client(
                username=settings.USERNAME,
                password=settings.PASSWORD,
                on_login=lambda x: callback.onlogin(x, settings_file),
                authenticate=False,
            )
        else:
            with open(settings_file) as file_data:
                cached_settings = json.load(file_data, object_hook=callback.from_json)

            logger.info(f"Reusing settings: {settings_file}")

            device_id = cached_settings.get("device_id")
            api = Client(
                username=settings.USERNAME,
                password=settings.PASSWORD,
                settings=cached_settings,
            )

    except (ClientCookieExpiredError, ClientLoginRequiredError) as e:
        # Login expired
        # Do relogin but use default ua, keys and such
        logger.error(f"ClientCookieExpiredError/ClientLoginRequiredError: {e}")
        logger.info(f"Logging back in with device_id: {device_id}")

        api = Client(
            username=settings.USERNAME,
            password=settings.PASSWORD,
            device_id=device_id,
            on_login=lambda x: callback.onlogin(x, settings_file),
            authenticate=False,
        )

    except ClientLoginError as e:
        logger.error(f"ClientLoginError {e}")
        raise

    except ClientError as e:
        logger.error(
            f"ClientError {e.msg} (Code: {e.code}, Response: {e.error_response})"
        )
        raise

    except Exception as e:
        logger.error(f"Unexpected Exception: {e}")
        raise

    return api
