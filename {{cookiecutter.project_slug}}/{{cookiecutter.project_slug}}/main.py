"""
Entrypoint for CLI.

This is the main entry point for the {{cookiecutter.project_name}} CLI application.
It provides configuration management capabilities through the config command.
"""
import typer

from {{cookiecutter.project_slug}}.commands import config

app = typer.Typer(
    no_args_is_help=True,
    help="{{cookiecutter.description}}",
    rich_markup_mode="rich",
)
app.add_typer(config.app, name="config")


def {{cookiecutter.cli_command}}():
    app()


if __name__ == "__main__":
    app()
