# Welcome to {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Installation

```bash
pip install {{cookiecutter.project_slug}}
```

## Usage

The CLI provides a `config` command for managing configuration settings:

```bash
{{cookiecutter.cli_command}} config --help
```

## Configuration Management

### Set Configuration Values

Set a configuration value directly:

```bash
{{cookiecutter.cli_command}} config set theme dark
{{cookiecutter.cli_command}} config set debug true
{{cookiecutter.cli_command}} config set timeout 30
```

Set a configuration value interactively (you'll be prompted for the value):

```bash
{{cookiecutter.cli_command}} config set custom_key
```

Values are automatically converted to appropriate types:
- `true`/`false` → boolean
- Numbers → integer or float
- Everything else → string

### Get Configuration Values

Retrieve a specific configuration value:

```bash
{{cookiecutter.cli_command}} config get theme
{{cookiecutter.cli_command}} config get debug
```

### List All Configuration

Display all configuration values in a formatted table:

```bash
{{cookiecutter.cli_command}} config list
```

### Reset Configuration

Reset all configuration to default values (with confirmation prompt):

```bash
{{cookiecutter.cli_command}} config reset
```

## Configuration Storage

Configuration is stored in a JSON file:
- Default location: `~/.acli_config.json`
- Custom location: Set `ACLI_CONFIG_PATH` environment variable

```bash
export ACLI_CONFIG_PATH=/path/to/my/config.json
{{cookiecutter.cli_command}} config set theme dark
```

## Default Configuration

The CLI comes with the following default configuration:

| Key | Value | Type | Description |
|-----|--------|------|-------------|
| `theme` | `default` | string | UI theme setting |
| `output_format` | `table` | string | Default output format |
| `auto_save` | `true` | boolean | Auto-save settings |
| `debug` | `false` | boolean | Debug mode |

## Examples

### Basic Configuration Setup

```bash
# View current configuration
{{cookiecutter.cli_command}} config list

# Set your preferred theme
{{cookiecutter.cli_command}} config set theme dark

# Enable debug mode
{{cookiecutter.cli_command}} config set debug true

# View updated configuration
{{cookiecutter.cli_command}} config list

# Get a specific value
{{cookiecutter.cli_command}} config get theme
```

### Using Custom Configuration Path

```bash
# Set custom config location
export ACLI_CONFIG_PATH="$HOME/my-project/.acli_config.json"

# Now all config commands use the custom location
{{cookiecutter.cli_command}} config set project_name "My Project"
{{cookiecutter.cli_command}} config list
```

### Resetting Configuration

```bash
# Reset to defaults (with confirmation)
{{cookiecutter.cli_command}} config reset

# Verify reset worked
{{cookiecutter.cli_command}} config list
```

## Error Handling

The CLI provides helpful error messages:

```bash
# Trying to get a non-existent key
$ {{cookiecutter.cli_command}} config get nonexistent
Error: Configuration key 'nonexistent' not found.

# Corrupted config file
$ {{cookiecutter.cli_command}} config get theme
Error: Configuration file /path/to/config.json is corrupted.
```

## Development

For developers who want to extend this CLI or use it as a template:

### Testing

Run the test suite:

```bash
pytest tests/ -v
```

### Building Documentation

Build the documentation locally:

```bash
mkdocs serve -f docs/mkdocs.yml
```

The CLI is built with:
- [Typer](https://typer.tiangolo.com/) - Modern CLI framework
- [Rich](https://rich.readthedocs.io/) - Rich text and beautiful formatting
- [Pytest](https://pytest.org/) - Testing framework

