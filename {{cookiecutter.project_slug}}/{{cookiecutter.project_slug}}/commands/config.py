"""
Configuration management command for the CLI.

This module provides commands to manage configuration settings stored in a JSON file.
The configuration file location can be customized via the ACLI_CONFIG_PATH environment variable.
"""
import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(
    no_args_is_help=True,
    help="Manage configuration settings for the CLI application.",
)

console = Console()

# Default configuration values
DEFAULT_CONFIG = {
    "theme": "default",
    "output_format": "table",
    "auto_save": True,
    "debug": False,
}


def get_config_path() -> Path:
    """
    Get the configuration file path.
    
    Returns the path from ACLI_CONFIG_PATH environment variable if set,
    otherwise returns the default path ~/.acli_config.json.
    
    Returns:
        Path: The configuration file path.
    """
    config_path = os.getenv("ACLI_CONFIG_PATH")
    if config_path:
        return Path(config_path)
    return Path.home() / ".acli_config.json"


def load_config() -> Dict[str, Any]:
    """
    Load configuration from the JSON file.
    
    If the file doesn't exist, returns the default configuration.
    
    Returns:
        Dict[str, Any]: The configuration dictionary.
        
    Raises:
        typer.Exit: If the configuration file is corrupted.
    """
    config_path = get_config_path()
    
    if not config_path.exists():
        return DEFAULT_CONFIG.copy()
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        return config
    except json.JSONDecodeError:
        console.print(f"[red]Error: Configuration file {config_path} is corrupted.[/red]")
        raise typer.Exit(1)
    except Exception as e:
        console.print(f"[red]Error reading configuration file: {e}[/red]")
        raise typer.Exit(1)


def save_config(config: Dict[str, Any]) -> None:
    """
    Save configuration to the JSON file.
    
    Args:
        config: The configuration dictionary to save.
        
    Raises:
        typer.Exit: If the configuration file cannot be written.
    """
    config_path = get_config_path()
    
    try:
        # Ensure the directory exists
        config_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        
        console.print(f"[green]Configuration saved to {config_path}[/green]")
    except Exception as e:
        console.print(f"[red]Error saving configuration file: {e}[/red]")
        raise typer.Exit(1)


@app.command()
def set(
    key: str = typer.Argument(..., help="Configuration key to set"),
    value: Optional[str] = typer.Argument(None, help="Configuration value to set (will prompt if not provided)"),
) -> None:
    """
    Set a configuration value.
    
    If the value is not provided as an argument, you will be prompted to enter it interactively.
    The value will be automatically converted to the appropriate type (bool, int, float, or string).
    
    Examples:
        acli config set theme dark
        acli config set debug true
        acli config set timeout 30
    """
    config = load_config()
    
    if value is None:
        value = typer.prompt(f"Enter value for '{key}'")
    
    # Try to convert value to appropriate type
    converted_value: Any = value
    if value.lower() in ('true', 'false'):
        converted_value = value.lower() == 'true'
    elif value.isdigit():
        converted_value = int(value)
    elif value.replace('.', '').isdigit():
        try:
            converted_value = float(value)
        except ValueError:
            pass  # Keep as string
    
    config[key] = converted_value
    save_config(config)
    
    console.print(f"[green]Set {key} = {converted_value}[/green]")


@app.command()
def get(
    key: str = typer.Argument(..., help="Configuration key to retrieve"),
) -> None:
    """
    Retrieve a configuration value.
    
    Shows the value of the specified configuration key. If the key doesn't exist,
    an error message is displayed and the command exits with status 1.
    
    Examples:
        acli config get theme
        acli config get debug
    """
    config = load_config()
    
    if key not in config:
        console.print(f"[red]Error: Configuration key '{key}' not found.[/red]")
        raise typer.Exit(1)
    
    value = config[key]
    console.print(f"{key} = {value}")


@app.command()
def list() -> None:
    """
    Display all configuration values in a formatted table.
    
    Shows all current configuration settings in a rich-formatted table,
    making it easy to see all settings at a glance.
    
    The table includes the configuration key, current value, and the value type.
    """
    config = load_config()
    
    if not config:
        console.print("[yellow]No configuration settings found.[/yellow]")
        return
    
    table = Table(title="Configuration Settings")
    table.add_column("Key", style="cyan", no_wrap=True)
    table.add_column("Value", style="green")
    table.add_column("Type", style="blue")
    
    for key, value in sorted(config.items()):
        table.add_row(key, str(value), type(value).__name__)
    
    console.print(table)


@app.command()
def reset() -> None:
    """
    Reset configuration to default values.
    
    This command will restore all configuration settings to their default values.
    A confirmation prompt is shown before proceeding to prevent accidental resets.
    
    Default values:
        - theme: default
        - output_format: table
        - auto_save: true
        - debug: false
    """
    if not typer.confirm("Are you sure you want to reset all configuration to defaults?"):
        console.print("[yellow]Reset cancelled.[/yellow]")
        return
    
    save_config(DEFAULT_CONFIG.copy())
    console.print("[green]Configuration reset to defaults.[/green]")


if __name__ == "__main__":
    app()