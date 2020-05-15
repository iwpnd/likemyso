import json
import os.path

from instagram_private_api import __version__ as client_version
from instagram_private_api import Client
from instagram_private_api import ClientCookieExpiredError
from instagram_private_api import ClientError
from instagram_private_api import ClientLoginError
from instagram_private_api import ClientLoginRequiredError
from loguru import logger

from likemygf import logincallback
from likemygf import settings


def login():
    """
    """

    logger.info("Client version: {0!s}".format(client_version))
    device_id = None

    try:
        settings_file = settings.CONFIGFILE

        if not os.path.isfile(settings_file):
            logger.error(f"Unable to find file: {settings_file}")

            api = Client(
                username=settings.USERNAME,
                password=settings.PASSWORD,
                on_login=lambda x: logincallback.onlogin_callback(x, settings_file),
                authenticate=False,
            )
        else:
            with open(settings_file) as file_data:
                cached_settings = json.load(
                    file_data, object_hook=logincallback.from_json
                )

            logger.info("Reusing settings: {0!s}".format(settings_file))

            device_id = cached_settings.get("device_id")
            api = Client(
                username=settings.USERNAME,
                password=settings.PASSWORD,
                settings=cached_settings,
            )

    except (ClientCookieExpiredError, ClientLoginRequiredError) as e:
        logger.error(f"ClientCookieExpiredError/ClientLoginRequiredError: {e}")

        # Login expired
        # Do relogin but use default ua, keys and such
        api = Client(
            username=settings.USERNAME,
            password=settings.PASSWORD,
            device_id=device_id,
            on_login=lambda x: logincallback.onlogin_callback(x, settings_file),
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
