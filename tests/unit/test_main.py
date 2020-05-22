import json

import pytest
from loguru import logger
from typer.testing import CliRunner

from likemyso import callback
from likemyso.main import app

runner = CliRunner()


def test_cli():
    """TODO: Docstring for test_cli.
    :returns: TODO

    """

    result = runner.invoke(app, ["start", "--help"])

    assert result.exit_code == 0


@pytest.mark.parametrize(
    "cli_arguments",
    [
        (
            "--username",
            "--password",
            "--settings-file",
            "--so-username",
            "--so-username",
            "--time-sleep",
            "--last-n-pictures",
        ),
        ("-u", "-p", "-s", "-so", "-so", "-ts", "-lnp"),
    ],
    indirect=True,
)
def test_cli_start_arguments(
    sleepless, monkeypatch, mock_client, mock_settings_file_content, cli_arguments
):
    with runner.isolated_filesystem():
        with open("config.json", "w") as f:
            json.dump(mock_settings_file_content, f, default=callback.to_json)

        monkeypatch.setattr("likemyso.likemyso.Client", mock_client)

        result = runner.invoke(
            app,
            [
                "start",
                cli_arguments.username,
                "test_username",
                cli_arguments.password,
                "test_password",
                cli_arguments.settingsfile,
                "config.json",
                cli_arguments.so_username1,
                "test_so",
                cli_arguments.so_username2,
                "test_so2",
                cli_arguments.time_sleep,
                5,
                cli_arguments.last_n_pictures,
                5,
            ],
        )

    assert result.exit_code == 0


def test_cli_username_password_default_settings(
    sleepless,
    mock_client,
    mock_delenv_credentials,
    mock_delenv_settings,
    mock_settings_file_content,
    monkeypatch,
):

    monkeypatch.setenv("INSTAGRAM_USERNAME", "test_user")
    monkeypatch.setenv("INSTAGRAM_PASSWORD", "test_password")

    monkeypatch.setattr("likemyso.likemyso.Client", mock_client)
    monkeypatch.setattr("likemyso.main.settings.users_to_like", [])

    with runner.isolated_filesystem():
        with open("config.json", "w") as f:
            json.dump(mock_settings_file_content, f, default=callback.to_json)

        result = runner.invoke(
            app,
            ["start", "-u", "test_user", "-p", "test_password", "-so", "test_user1"],
        )

    logger.debug(f"result: {result.__dict__}")

    assert result.exit_code == 0


@pytest.mark.parametrize(
    "arguments",
    [
        pytest.param(
            ["start", "-u", "test_user", "-so", "test_user1"], id="no password"
        ),
        pytest.param(
            ["start", "-p", "test_password", "-so", "test_user1"], id="no username"
        ),
    ],
)
def test_cli_no_required_input(
    sleepless,
    mock_client,
    mock_delenv_credentials,
    mock_delenv_settings,
    mock_settings_file_content,
    monkeypatch,
    arguments,
):

    monkeypatch.setenv("INSTAGRAM_USERNAME", "test_user")
    monkeypatch.setenv("INSTAGRAM_PASSWORD", "test_password")
    monkeypatch.setattr("likemyso.likemyso.Client", mock_client)
    with runner.isolated_filesystem():
        with open("config.json", "w") as f:
            json.dump(mock_settings_file_content, f, default=callback.to_json)

        result = runner.invoke(app, arguments)

    logger.debug(f"result: {result.__dict__}")
    assert result.exit_code == 2


@pytest.mark.parametrize(
    "arguments",
    [pytest.param(["start", "-p", "test_password", "-u", "test_user"], id="no so")],
)
def test_cli_no_so(
    sleepless,
    mock_client,
    mock_delenv_credentials,
    mock_delenv_settings,
    mock_settings_file_content,
    monkeypatch,
    arguments,
):

    monkeypatch.setenv("INSTAGRAM_USERNAME", "test_user")
    monkeypatch.setenv("INSTAGRAM_PASSWORD", "test_password")
    monkeypatch.setattr("likemyso.likemyso.Client", mock_client)
    # monkeypatch.setattr("likemyso.main.settings.users_to_like", [])

    with runner.isolated_filesystem():
        with open("config.json", "w") as f:
            json.dump(mock_settings_file_content, f, default=callback.to_json)

        result = runner.invoke(app, arguments)

    logger.debug(f"result: {result.__dict__}")

    assert result.exit_code == 2
