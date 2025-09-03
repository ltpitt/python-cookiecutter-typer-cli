FROM python:3.12-slim

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -e .

ENTRYPOINT [ "{{cookiecutter.cli_command.strip().lower().replace(' ', '_').replace('-', '_')}}" ]
