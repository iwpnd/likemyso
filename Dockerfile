FROM python:3.7-alpine

WORKDIR /code
RUN apk add --no-cache git

# dont write pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# dont buffer to stdout/stderr
ENV PYTHONUNBUFFERED 1

COPY . /code

# dependencies
RUN set -eux \
    && pip install --upgrade pip setuptools wheel \
    && pip install git+https://github.com/iwpnd/instagram_private_api.git \
    && pip install -e /code \
    && rm -rf /root/.cache/pip
