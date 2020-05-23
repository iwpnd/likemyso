import time

import pytest


class CliArguments(object):
    def __init__(
        self,
        username: str,
        password: str,
        settingsfile: str,
        so_username1: str,
        so_username2: str,
        time_sleep: int,
        last_n_pictures: int,
    ) -> None:
        self.username = username
        self.password = password
        self.settingsfile = settingsfile
        self.so_username1 = so_username1
        self.so_username2 = so_username2
        self.time_sleep = time_sleep
        self.last_n_pictures = last_n_pictures


@pytest.fixture
def cli_arguments(request):
    cliargs = CliArguments(*request.param)
    return cliargs


@pytest.fixture
def sleepless(monkeypatch):
    def sleep(seconds):
        pass

    monkeypatch.setattr(time, "sleep", sleep)


class MockClient:

    settings = {
        "uuid": "40f64706-9685-11ea-a310-60f71db537ec",
        "device_id": "android-40f6499a966511ea",
        "ad_id": "963489a6-b820-1d20-62ef-25d72a0a0680",
        "session_id": "40f64a76-9685-11ea-a311-60f81db537ec",
        "cookie": b"\x80\x03",
        "created_ts": 1589537039,
    }

    def __init__(
        self,
        username="test",
        password="test",
        on_login=False,
        authenticate=False,
        settings=False,
    ):
        if on_login:
            on_login(self)

    def username_feed(self, user_name: str):
        return {
            "items": [
                {
                    "taken_at": 1589630436,
                    "id": "2310309123501019499_3552842274",
                    "has_liked": False,
                },
                {
                    "taken_at": 1589551274,
                    "id": "2309645417974902256_3552842274",
                    "has_liked": True,
                },
            ],
            "num_results": 2,
        }

    def post_like(self, media_id: str):
        return True


@pytest.fixture
def mock_client():
    return MockClient


@pytest.fixture
def mock_instagram_api_client():
    class MockClient:

        settings = {
            "uuid": "40f64706-9685-11ea-a310-60f71db537ec",
            "device_id": "android-40f6499a966511ea",
            "ad_id": "963489a6-b820-1d20-62ef-25d72a0a0680",
            "session_id": "40f64a76-9685-11ea-a311-60f81db537ec",
            "cookie": b"\x80\x03",
            "created_ts": 1589537039,
        }

    mock_client = MockClient()

    return mock_client


@pytest.fixture
def mock_settings_file_content():
    return {
        "uuid": "40f64706-9685-11ea-a310-60f71db537ec",
        "device_id": "android-40f6499a966511ea",
        "ad_id": "963489a6-b820-1d20-62ef-25d72a0a0680",
        "session_id": "40f64a76-9685-11ea-a311-60f81db537ec",
        "cookie": b"\x80\x03",
        "created_ts": 1589537039,
    }


@pytest.fixture
def mock_delenv_settings(monkeypatch):
    monkeypatch.delenv("INSTAGRAM_SETTINGS_FILE", raising=False)
    monkeypatch.delenv("INSTAGRAM_USERS_TO_LIKE", raising=False)
    monkeypatch.delenv("INSTAGRAM_LAST_N_PICTURES", raising=False)
    monkeypatch.delenv("INSTAGRAM_TIME_SLEEP_BETWEEN_CALLS", raising=False)


@pytest.fixture
def mock_delenv_credentials(monkeypatch):
    monkeypatch.delenv("INSTAGRAM_USERNAME", raising=False)
    monkeypatch.delenv("INSTAGRAM_PASSWORD", raising=False)
