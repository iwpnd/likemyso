import typer

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
        ...,
        "--settings-file",
        "-s",
        help="your instagram settins file, if you have previously logged",
    ),
    significant_other: str = typer.Option(
        ..., "--so-username", "-so", help="your significant others username"
    ),
):
    pass
