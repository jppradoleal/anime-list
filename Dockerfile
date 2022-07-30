FROM python:3.9

# Sys deps
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    wait-for-it

WORKDIR /django
COPY pyproject.toml poetry.lock /django/
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry config --list
RUN poetry install
COPY . .