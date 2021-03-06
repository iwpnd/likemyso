# likemySO

Like your significant others latest instagram pictures if you forgot it (again). Build on [instagram_private_api](https://github.com/ping/instagram_private_api) based on the idea of [Like-My-GF](https://github.com/cyandterry/Like-My-GF).

## Usage

```python
from likemyso import InstaHusband # InstaWife

instahusband = Instahusband()
instahusband.login(username="your_username", password="your_password")

instahusband.like(
    significant_other="your_SOs_username",
    last_n_pictures=5,
    time_sleep_between_calls=20
    )
```

This will log you into instagram, get the latest items from your SO's instagram feed and like the images that you ""forgot"" to like. Your session will be stored in a settingsfile to [avoid re-logins](https://instagram-private-api.readthedocs.io/en/latest/usage.html#avoiding-re-login) that might flag your instagram account and/or gets you banned.

## Installation
### prerequisites

create and activate a virtual environment in your working directory:
```bash
virtualenv env
source env/bin/activate
```
### installation

clone and install the repository:
```bash
git clone https://github.com/iwpnd/likemyso.git
pip install -e /likemyso
```

### testing
```bash
pytest . --cov=likemyso/likemyso -v
```

#### optionally:

create a `.env` file in your working directory:

```bash
# .env
INSTAGRAM_USERNAME=your_username
INSTAGRAM_PASSWORD=your_password
INSTAGRAM_SETTINGS_FILE=config.json
INSTAGRAM_USERS_TO_LIKE='["significant_other"]'
INSTAGRAM_LAST_N_PICTURES=5
INSTAGRAM_TIME_SLEEP_BETWEEN_CALLS=20
```


## CLI and CronJob

```bash
Usage: likemyso start [OPTIONS]

Options:
  -u, --username TEXT             your instagram username

  -p, --password TEXT             your instagram password

  -s, --settings-file TEXT        your instagram settings file, if you have
                                  previously logged, defaults to
                                  settings.settings_file

  -so, --so-username TEXT         your significant others username
  -ts, --time-sleep INTEGER       time sleep between api calls, defaults to
                                  settings.time_sleep_between_calls

  -lnp, --last-n-pictures INTEGER
                                  last n pictures to like in your SOs
                                  instagram feed, defaults to
                                  settings.last_n_pictures

  --help                          Show this message and exit.
```

I run this as a service on my raspberry pi in a Docker Swarm Cluster using [swarm-cronjob](https://github.com/crazy-max/swarm-cronjob) to schedule a re-run every now and then.

## Disclaimer

This is not affliated, endorsed or certified by Instagram. This uses is an [independent and unofficial API](https://github.com/ping/instagram_private_api). Strictly not for spam. Use at your own risk.
