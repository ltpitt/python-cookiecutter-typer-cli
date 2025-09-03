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

### Setup

1. **Create virtual environment**:
   ```bash
   make venv
   source venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   make install
   ```

3. **Install pre-commit hooks**:
   ```bash
   make pre-commit
   ```

### Testing

Run the comprehensive test suite:

```bash
make test
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

3. **View documentation**: Open http://localhost:8000

### Code Quality

- **Format code**: `make format`
- **Check formatting**: `make check`
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

2. **Upload to PyPI**:
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
