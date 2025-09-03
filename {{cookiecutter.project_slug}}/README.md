# {{cookiecutter.project_name}}

{{cookiecutter.description}}

This CLI tool provides configuration management capabilities with a clean, modern interface built using Typer and Rich.

## Features

- **Configuration Management**: Set, get, list, and reset configuration values
- **Type-aware Values**: Automatic conversion of boolean, numeric, and string values
- **Rich Formatting**: Beautiful table output and colorized messages
- **Interactive Prompts**: Set values interactively when not provided
- **Environment Support**: Custom config file location via `ACLI_CONFIG_PATH`
- **Comprehensive Testing**: Full test suite with pytest
- **Professional Documentation**: Auto-generated docs with MkDocs

## Quick Start

1. **Installation**: Install the package in development mode
   ```bash
   cd {{cookiecutter.project_slug}}
   make install
   ```

2. **Basic Usage**: Try the configuration commands
   ```bash
   {{cookiecutter.cli_command}} config list
   {{cookiecutter.cli_command}} config set theme dark
   {{cookiecutter.cli_command}} config get theme
   ```

## CLI Commands

### Configuration Management

- **`{{cookiecutter.cli_command}} config set KEY VALUE`** - Set a configuration value
- **`{{cookiecutter.cli_command}} config get KEY`** - Get a configuration value  
- **`{{cookiecutter.cli_command}} config list`** - List all configuration values
- **`{{cookiecutter.cli_command}} config reset`** - Reset to default values

### Examples

```bash
# View current configuration
{{cookiecutter.cli_command}} config list

# Set values directly
{{cookiecutter.cli_command}} config set theme dark
{{cookiecutter.cli_command}} config set debug true
{{cookiecutter.cli_command}} config set timeout 30

# Set values interactively
{{cookiecutter.cli_command}} config set custom_key
# > Enter value for 'custom_key': my_value

# Get specific values
{{cookiecutter.cli_command}} config get theme
{{cookiecutter.cli_command}} config get debug

# Reset to defaults (with confirmation)
{{cookiecutter.cli_command}} config reset
```

## Development

### Prerequisites

This project uses [Poetry](https://python-poetry.org/) for dependency management. Install Poetry first:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Setup

1. **Install dependencies**:
   ```bash
   make install
   ```
   This installs the package and all development dependencies using Poetry.

2. **Install pre-commit hooks**:
   ```bash
   make pre-commit
   ```

### Testing

Run the comprehensive test suite:

```bash
make test
```

Or run tests directly with Poetry:

```bash
poetry run pytest -vvv
```

Tests cover:
- All config subcommands (set, get, list, reset)
- Type conversion (boolean, numeric, string)
- Error handling (missing keys, corrupted files)
- Interactive prompts and confirmations
- Environment variable configuration
- File creation and management

### Documentation

1. **Install docs dependencies**:
   ```bash
   make docs
   ```

2. **Serve docs locally**:
   ```bash
   make serve-docs
   ```
   Or run directly with Poetry:
   ```bash
   poetry run mkdocs serve -f docs/mkdocs.yml
   ```

3. **View documentation**: Open http://localhost:8000

### Code Quality

- **Format code**: `make format` or `poetry run black .`
- **Check formatting**: `make check` or `poetry run black --check --diff .`
- **Run linting**: `poetry run flake8`
- **Type checking**: `poetry run mypy .`
- **Clean artifacts**: `make clean`

### Docker Testing

Test the CLI in a clean container environment:

1. **Build image**:
   ```bash
   make docker-image
   ```

2. **Run commands**:
   ```bash
   docker run --rm {{cookiecutter.cli_command}} config list
   ```

## Configuration Storage

- **Default location**: `~/.acli_config.json`
- **Custom location**: Set `ACLI_CONFIG_PATH` environment variable
- **Format**: JSON with automatic type preservation
- **Default values**: Includes theme, output_format, auto_save, and debug settings

## Distribution

### PyPI Publishing

> **NOTE**: Ensure you have a [PyPI account](https://pypi.org/account/register/) before publishing.

1. **Create distributions**:
   ```bash
   make distributions
   ```
   This builds the package using Poetry.

2. **Upload to PyPI**:
   ```bash
   poetry publish
   ```
   Or use twine:
   ```bash
   twine upload dist/*
   ```

### Package Structure

The generated package includes:
- **Clean CLI interface** with professional help text
- **Comprehensive test coverage** for all functionality
- **Type-safe configuration handling** with automatic conversions
- **Rich formatting** for beautiful output
- **Professional documentation** ready for deployment
- **Docker support** for containerized usage

## Architecture

Built with modern Python CLI best practices:

- **[Poetry](https://python-poetry.org/)** - Modern dependency management
- **[Typer](https://typer.tiangolo.com/)** - Type-based CLI framework
- **[Rich](https://rich.readthedocs.io/)** - Beautiful terminal output
- **[Pytest](https://pytest.org/)** - Reliable testing framework
- **[MkDocs](https://mkdocs.org/)** - Professional documentation
- **[Black](https://black.readthedocs.io/)** - Code formatting
- **[Pre-commit](https://pre-commit.com/)** - Git hooks for quality

## Help

View all available make commands:

```bash
make help
```

Get CLI help:

```bash
{{cookiecutter.cli_command}} --help
{{cookiecutter.cli_command}} config --help
```
