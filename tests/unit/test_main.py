from typer.testing import CliRunner

from likemyso.main import app

runner = CliRunner()


def test_cli():
    """TODO: Docstring for test_cli.
    :returns: TODO

    """

    result = runner.invoke(app, ["start", "--help"])

    assert result.exit_code == 0


def test_cli_start_arguments():
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
        ],
    )

    assert result.exit_code == 0


def test_cli_start_arguments_short():
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
        ],
    )

    assert result.exit_code == 0
