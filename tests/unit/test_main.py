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
        with open("test_config.json", "w") as f:
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
                "test_config.json",
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
