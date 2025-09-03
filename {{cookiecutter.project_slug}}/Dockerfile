FROM python:3.12-slim

# Install Poetry
RUN pip install poetry

# Configure Poetry: do not create virtual env (we're in a container)
ENV POETRY_VENV_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1

COPY . /app

WORKDIR /app

# Install dependencies using Poetry
RUN poetry install --only main

ENTRYPOINT [ "poetry", "run", "{{cookiecutter.cli_command.strip().lower().replace(' ', '_').replace('-', '_')}}" ]
