# Pull base image
FROM python:3.11

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install pip and poetry
RUN pip install --upgrade pip
RUN pip install poetry

# Set work directory
WORKDIR /code

# Copy only requirements to cache them in docker layer
COPY pyproject.toml poetry.lock /code/

# Project initialization:
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Installing netcat
RUN apt-get update && apt-get install -y netcat-openbsd

# Copy entrypoint.sh
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Copy project
COPY . /code/

# chown all the files to the app user
RUN useradd -M master -s /bin/false
RUN chown -R master:master /code

# change to the app user
USER master

EXPOSE 8000

# Run the application:
CMD ["/entrypoint.sh", "db"]
