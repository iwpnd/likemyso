import time
from typing import List

import typer
from loguru import logger

from likemyso import InstaHusband
from likemyso import settings

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
        ...,
        "--password",
        "-p",
        help="your instagram password",
        prompt=False,
        hide_input=True,
    ),
    settings_file: str = typer.Option(
        settings.SETTINGSFILE,
        "--settings-file",
        "-s",
        help="your instagram settings file, if you have previously logged",
    ),
    significant_other: List[str] = typer.Option(
        ..., "--so-username", "-so", help="your significant others username"
    ),
):
    instahusband = InstaHusband()
    instahusband.login(
        username=username, password=password, settings_file=settings_file
    )

    for so in significant_other:
        logger.info(f"Checking {so} for new pictures")
        instahusband.like(significant_other=so)
        time.sleep(settings.TIME_SLEEP_BETWEEN_CALLS)
