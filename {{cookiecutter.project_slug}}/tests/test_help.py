from typer.testing import CliRunner
from {{cookiecutter.project_slug}}.main import app

runner = CliRunner()


def test_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Usage: " in result.output
