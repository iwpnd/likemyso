import json

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


def test_cli_start_arguments(
    sleepless, monkeypatch, mock_client, mock_settings_file_content
):
    with runner.isolated_filesystem():
        with open("test_config.json", "w") as f:
            json.dump(mock_settings_file_content, f, default=callback.to_json)

        monkeypatch.setattr("likemyso.likemyso.Client", mock_client)

        result = runner.invoke(
            app,
            [
                "start",
                "--username",
                "test_username",
                "--password",
                "test_password",
                "--settings-file",
                "test_config.json",
                "--so-username",
                "test_so",
                "--so-username",
                "test_so2",
            ],
        )

        assert result.exit_code == 0


def test_cli_start_arguments_short(
    monkeypatch, mock_client, mock_settings_file_content, sleepless
):
    with runner.isolated_filesystem():
        with open("test_config.json", "w") as f:
            json.dump(mock_settings_file_content, f, default=callback.to_json)

        monkeypatch.setattr("likemyso.likemyso.Client", mock_client)

        result = runner.invoke(
            app,
            [
                "start",
                "-u",
                "test_username",
                "-p",
                "test_password",
                "-s",
                "test_config.json",
                "-so",
                "test_so",
                "-so",
                "test_so2",
            ],
        )

        assert result.exit_code == 0
