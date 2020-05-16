import pytest


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
