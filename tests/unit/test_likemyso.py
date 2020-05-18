import json
import os

from likemyso import callback
from likemyso import likemyso


def test_init_instahusband():
    instahusband = likemyso.InstaHusband()

    assert instahusband


def test_init_instawife():
    instawaifu = likemyso.InstaWife()

    assert instawaifu


def test_instahusband_login_nosettingsfile(tmpdir, monkeypatch, mock_client):

    monkeypatch.setattr("likemyso.likemyso.Client", mock_client)

    settings_file = tmpdir.join("test_config.json")

    instahusband = likemyso.InstaHusband()
    instahusband.login(username="test", password="test", settings_file=settings_file)

    assert hasattr(instahusband, "api")
    assert os.path.exists(settings_file.strpath)


def test_instahusband_login_settingsfile(
    tmpdir, monkeypatch, mock_settings_file_content, mock_client
):

    monkeypatch.setattr("likemyso.likemyso.Client", mock_client)

    settings_file = tmpdir.join("test_config.json")

    with open(settings_file, "w") as f:
        json.dump(mock_settings_file_content, f, default=callback.to_json)

    instahusband = likemyso.InstaHusband()
    instahusband.login(username="test", password="test", settings_file=settings_file)

    assert hasattr(instahusband, "api")
    assert os.path.exists(settings_file.strpath)


def test_instahusband_get_feed(tmpdir, monkeypatch, mock_client):

    settings_file = tmpdir.join("test_config.json")

    monkeypatch.setattr("likemyso.likemyso.Client", mock_client)

    instahusband = likemyso.InstaHusband()
    instahusband.login(username="test", password="test", settings_file=settings_file)

    feed = instahusband.get_feed(username="testuser")

    assert feed.dict()


def test_instahusband_like(tmpdir, monkeypatch, mock_client):

    settings_file = tmpdir.join("test_config.json")

    monkeypatch.setattr("likemyso.likemyso.Client", mock_client)

    instahusband = likemyso.InstaHusband()
    instahusband.login(username="test", password="test", settings_file=settings_file)
    instahusband.like(
        significant_other="testuser", last_n_pictures=2, time_sleep_between_calls=0
    )
