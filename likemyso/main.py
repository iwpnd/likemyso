import time
from typing import List

import typer
from loguru import logger

from likemyso import InstaHusband
from likemyso.config import Credentials
from likemyso.config import Settings

settings = Settings()
logger.debug(settings.json())

app = typer.Typer()


@app.callback()
def callback():
    """
    be a good instaSO and like your SOs instagram pictures from the CLI

    Arguments:
    Returns:
    """
    pass


@app.command()
def start(
    username: str = typer.Option(
        ..., "--username", "-u", help="your instagram username"
    ),
    password: str = typer.Option(
        ..., "--password", "-p", help="your instagram password"
    ),
    significant_other: List[str] = typer.Option(
        "",
        "--so-username",
        "-so",
        help="your significant others username",
        show_default=True,
    ),
    settings_file: str = typer.Option(
        settings.settings_file,
        "--settings-file",
        "-s",
        help="your instagram settings file, if you have previously logged, defaults to settings.file",
        show_default=True,
    ),
    time_sleep_between_calls: int = typer.Option(
        settings.time_sleep_between_calls,
        "--time-sleep",
        "-ts",
        help="time sleep between api calls, defaults to settings.time_sleep_between_calls",
        show_default=True,
    ),
    last_n_pictures: int = typer.Option(
        settings.last_n_pictures,
        "--last-n-pictures",
        "-lnp",
        help="last n pictures to like in your SOs instagram feed, defaults to settings.last_n_pictures",
        show_default=True,
    ),
):

    # either use args or settings, if neither raise
    significant_other = significant_other or settings.users_to_like

    # if significant_other = ('',), because bool(('',)) == True
    try:
        if not significant_other[0]:
            raise typer.Exit(code=6)
    except IndexError:
        raise typer.Exit(code=6)

    credentials = Credentials(username=username, password=password)

    logger.info(settings.json())
    instahusband = InstaHusband()
    instahusband.login(
        username=credentials.username,
        password=credentials.password.get_secret_value(),
        settings_file=settings.settings_file,
    )

    for so in significant_other:
        instahusband.like(
            significant_other=so,
            time_sleep_between_calls=settings.time_sleep_between_calls,
            last_n_pictures=settings.last_n_pictures,
        )
        time.sleep(settings.time_sleep_between_calls)
