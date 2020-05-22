import pytest
from pydantic import ValidationError

from likemyso.settings import Credentials
from likemyso.settings import Settings


def test_credentials_from_env(monkeypatch):
    monkeypatch.setenv("INSTAGRAM_USERNAME", "test_user")
    monkeypatch.setenv("INSTAGRAM_PASSWORD", "test_password")
    credentials = Credentials()

    assert credentials.username == "test_user"
    assert credentials.password.get_secret_value() == "test_password"


def test_credentials_from_args(mock_delenv_credentials):
    credentials = Credentials(username="test_username", password="test_password")

    assert credentials.username == "test_username"
    assert credentials.password.get_secret_value() == "test_password"


def test_credentials_raises(mock_delenv_credentials):

    with pytest.raises(ValidationError):
        credentials = Credentials()

        assert credentials


def test_settings_from_env(monkeypatch):

    monkeypatch.setenv("INSTAGRAM_SETTINGS_FILE", "test_config.json")
    monkeypatch.setenv("INSTAGRAM_USERS_TO_LIKE", '["test_user1", "test_user2"]')
    monkeypatch.setenv("INSTAGRAM_LAST_N_PICTURES", "1337")
    monkeypatch.setenv("INSTAGRAM_TIME_SLEEP_BETWEEN_CALLS", "1337")

    settings = Settings()

    assert settings.settings_file == "test_config.json"
    assert settings.users_to_like == ["test_user1", "test_user2"]
    assert settings.last_n_pictures == 1337
    assert settings.time_sleep_between_calls == 1337


def test_settings_from_args(mock_delenv_settings):
    settings = Settings(
        settings_file="test_config.json",
        users_to_like=["test_user1", "test_user2"],
        last_n_pictures=1337,
        time_sleep_between_calls=1337,
    )

    assert settings.settings_file == "test_config.json"
    assert settings.users_to_like == ["test_user1", "test_user2"]
    assert settings.last_n_pictures == 1337
    assert settings.time_sleep_between_calls == 1337


def test_settings_default_values(mock_delenv_settings):
    settings = Settings()

    assert settings.settings_file == "config.json"
    assert settings.users_to_like == []
    assert settings.last_n_pictures == 5
    assert settings.time_sleep_between_calls == 20
