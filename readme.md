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

#### optionally:

create a `.env` file in your working directory:

```bash
# .env
USERNAME=your_username
PASSWORD=your_password
SETTINGSFILE=config.json
USERS_TO_LIKE=your_SO_username
LAST_N_PICTURES=5
TIME_SLEEP_BETWEEN_CALLS=20
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

## CLI and CronJob

**SOON**

```bash
likemyso start
```

I run this as a service on my raspberry pi in a Docker Swarm Cluster using [swarm-cronjob](https://github.com/crazy-max/swarm-cronjob) to schedule a re-run every now and then.

## Disclaimer

This is not affliated, endorsed or certified by Instagram. This uses is an [independent and unofficial API](https://github.com/ping/instagram_private_api). Strictly not for spam. Use at your own risk.
