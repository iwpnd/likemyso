import pytest


def mock_time_sleep(seconds):
    return None


@pytest.fixture
def mock_sleep():
    return mock_time_sleep


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
