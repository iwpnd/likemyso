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
        settings.INSTAGRAM_USERNAME,
        "--username",
        "-u",
        help="your instagram username, defaults to settings.INSTAGRAM_USERNAME",
    ),
    password: str = typer.Option(
        settings.INSTAGRAM_PASSWORD,
        "--password",
        "-p",
        help="your instagram password, defaults to settings.INSTAGRAM_PASSWORD",
        prompt=False,
        hide_input=True,
    ),
    settings_file: str = typer.Option(
        settings.SETTINGSFILE,
        "--settings-file",
        "-s",
        help="your instagram settings file, if you have previously logged, defaults to settings.SETTINGSFILE",
    ),
    significant_other: List[str] = typer.Option(
        "", "--so-username", "-so", help="your significant others username"
    ),
    time_sleep_between_calls: int = typer.Option(
        settings.TIME_SLEEP_BETWEEN_CALLS,
        "--time-sleep",
        "-ts",
        help="time sleep between api calls, defaults to settings.TIME_SLEEP_BETWEEN_CALLS",
    ),
    last_n_pictures: int = typer.Option(
        settings.LAST_N_PICTURES,
        "--last-n-pictures",
        "-lnp",
        help="last n pictures to like in your SOs instagram feed, defaults to settings.LAST_N_PICTURES",
    ),
):
    if not (significant_other or settings.USERS_TO_LIKE[0]):
        raise typer.Exit(code=13)

    instahusband = InstaHusband()
    instahusband.login(
        username=username, password=password, settings_file=settings_file
    )

    if significant_other:
        logger.info(f"Significant other: {significant_other}")
        for so in significant_other:
            logger.info(f"Checking {so} for new pictures")
            instahusband.like(
                significant_other=so,
                time_sleep_between_calls=time_sleep_between_calls,
                last_n_pictures=last_n_pictures,
            )
            time.sleep(settings.TIME_SLEEP_BETWEEN_CALLS)
    else:
        logger.info(
            f"Significant other from settings.USERS_TO_LIKE: {settings.USERS_TO_LIKE}"
        )
        for so in settings.USERS_TO_LIKE:
            logger.info(f"Checking {so} for new pictures")
            instahusband.like(
                significant_other=so,
                time_sleep_between_calls=time_sleep_between_calls,
                last_n_pictures=last_n_pictures,
            )
            time.sleep(settings.TIME_SLEEP_BETWEEN_CALLS)
