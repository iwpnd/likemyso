import time
from typing import List

import typer
from loguru import logger

from likemyso import InstaHusband
from likemyso.settings import settings

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
        settings.username,
        "--username",
        "-u",
        help="your instagram username, defaults to settings.username",
    ),
    password: str = typer.Option(
        settings.password.get_secret_value(),
        "--password",
        "-p",
        help="your instagram password, defaults to settings.password.get_secret_value()",
        prompt=False,
        hide_input=True,
    ),
    settings_file: str = typer.Option(
        settings.file,
        "--settings-file",
        "-s",
        help="your instagram settings file, if you have previously logged, defaults to settings.file",
    ),
    significant_other: List[str] = typer.Option(
        "", "--so-username", "-so", help="your significant others username"
    ),
    time_sleep_between_calls: int = typer.Option(
        settings.time_sleep_between_calls,
        "--time-sleep",
        "-ts",
        help="time sleep between api calls, defaults to settings.time_sleep_between_calls",
    ),
    last_n_pictures: int = typer.Option(
        settings.last_n_pictures,
        "--last-n-pictures",
        "-lnp",
        help="last n pictures to like in your SOs instagram feed, defaults to settings.last_n_pictures",
    ),
):
    if not (significant_other or settings.users_to_like):
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
            time.sleep(settings.time_sleep_between_calls)
    else:
        logger.info(
            f"Significant other from settings.users_to_like: {settings.users_to_like}"
        )
        for so in settings.users_to_like:
            logger.info(f"Checking {so} for new pictures")
            instahusband.like(
                significant_other=so,
                time_sleep_between_calls=time_sleep_between_calls,
                last_n_pictures=last_n_pictures,
            )
            time.sleep(settings.time_sleep_between_calls)
