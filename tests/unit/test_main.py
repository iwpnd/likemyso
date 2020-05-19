import json

import pytest
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
    "username, password, settingsfile, so_username1, so_username2, time_sleep, last_n_pictures",
    [
        pytest.param(
            "--username",
            "--password",
            "--settings-file",
            "--so-username",
            "--so-username",
            "--time_sleep",
            "--last-n-pictures",
            id="long args",
        ),
        pytest.param("-u", "-p", "-s", "-so", "-so", "-ts", "-lnp", id="short args"),
    ],
)
def test_cli_start_arguments(
    sleepless,
    monkeypatch,
    mock_client,
    mock_settings_file_content,
    username,
    password,
    settingsfile,
    so_username1,
    so_username2,
    time_sleep,
    last_n_pictures,
):
    with runner.isolated_filesystem():
        with open("test_config.json", "w") as f:
            json.dump(mock_settings_file_content, f, default=callback.to_json)

        monkeypatch.setattr("likemyso.likemyso.Client", mock_client)

        result = runner.invoke(
            app,
            [
                "start",
                username,
                "test_username",
                password,
                "test_password",
                settingsfile,
                "test_config.json",
                so_username1,
                "test_so",
                so_username2,
                "test_so2",
            ],
        )

        assert result.exit_code == 0
