import json
import os.path
import time

from instagram_private_api import Client
from instagram_private_api import ClientCookieExpiredError
from instagram_private_api import ClientError
from instagram_private_api import ClientLoginError
from instagram_private_api import ClientLoginRequiredError
from loguru import logger

from likemyso import callback
from likemyso.config import Settings
from likemyso.models import SignificantOther
from likemyso.models import UserFeed

settings = Settings()


class InstaHusband:
    """
    """

    def __init__(self):
        pass

    def get_feed(self, username: str) -> UserFeed:
        try:
            return UserFeed(**self.api.username_feed(user_name=username))
        except Exception as e:
            logger.error(f"Exception: {e}")
            raise

    def like(
        self,
        significant_other: str,
        last_n_pictures: int = settings.last_n_pictures,
        time_sleep_between_calls: int = settings.time_sleep_between_calls,
    ):

        so = SignificantOther(
            name=significant_other,
            latest_feed=self.get_feed(username=significant_other),
        )
        logger.info(f"Checking pictures of user: {so.name}")

        for picture in so.latest_feed.items[:last_n_pictures]:
            if not picture.has_liked:
                self.api.post_like(picture.media_id)
                logger.info(f"Liked {picture.media_id} of user: {so.name}")
                time.sleep(time_sleep_between_calls)

    def login(
        self, username: str, password: str, settings_file: str = settings.settings_file
    ) -> Client:
        """ Authenticate with instagram API and prevent re-login if possible
        see: https://instagram-private-api.readthedocs.io/en/latest/usage.html#avoiding-re-login

        1. check if old settings can be found at settings.settings_file

        if yes:
            use old settings and cookies
                if is_expired: log back in with device_id and store to settings.settings_file

        if no:
            login with username and password

        Returns:
                Client
        """

        device_id = None
        logger.info(f"Log-in to {username}")

        try:
            if not os.path.isfile(settings_file):
                logger.error(f"Unable to find file: {settings_file}")

                self.api = Client(
                    username=username,
                    password=password,
                    on_login=lambda x: callback.onlogin(x, settings_file),
                    authenticate=False,
                )

            else:
                with open(settings_file) as file_data:
                    cached_settings = json.load(
                        file_data, object_hook=callback.from_json
                    )

                logger.info(f"Reusing settings: {settings_file}")

                device_id = cached_settings.get("device_id")
                self.api = Client(
                    username=username, password=password, settings=cached_settings
                )

        except (ClientCookieExpiredError, ClientLoginRequiredError) as e:
            # Login expired
            # Do relogin but use default ua, keys and such
            logger.error(f"ClientCookieExpiredError/ClientLoginRequiredError: {e}")
            logger.info(f"Logging back in with device_id: {device_id}")

            self.api = Client(
                username=username,
                password=password,
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


class InstaWife(InstaHusband):
    pass
