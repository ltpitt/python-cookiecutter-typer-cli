"""
Entrypoint for CLI.
"""
import typer

from {{cookiecutter.project_slug}}.commands import users, items

app = typer.Typer()
app.add_typer(users.app, name="users")
app.add_typer(items.app, name="items")


def {{cookiecutter.cli_command}}():
    app()


if __name__ == "__main__":
    app()
