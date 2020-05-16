import json
import os

from likemyso import callback
from likemyso import likemyso


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


def test_init_instahusband():
    instahusband = likemyso.InstaHusband()

    assert instahusband


def test_init_instawife():
    instawaifu = likemyso.InstaWife()

    assert instawaifu


def test_instahusband_login_nosettingsfile(tmpdir, monkeypatch):

    monkeypatch.setattr("likemyso.likemyso.Client", MockClient)

    settings_file = tmpdir.join("test_config.json")

    instahusband = likemyso.InstaHusband()
    instahusband.login(username="test", password="test", settings_file=settings_file)

    assert hasattr(instahusband, "api")
    assert os.path.exists(settings_file.strpath)


def test_instahusband_login_settingsfile(
    tmpdir, monkeypatch, mock_settings_file_content
):

    monkeypatch.setattr("likemyso.likemyso.Client", MockClient)

    settings_file = tmpdir.join("test_config.json")

    with open(settings_file, "w") as f:
        json.dump(mock_settings_file_content, f, default=callback.to_json)

    instahusband = likemyso.InstaHusband()
    instahusband.login(username="test", password="test", settings_file=settings_file)

    assert hasattr(instahusband, "api")
    assert os.path.exists(settings_file.strpath)
