"""
Test suite for the CLI application.

This module contains comprehensive tests for all CLI commands and functionality.
"""
import json
import os
import tempfile
from pathlib import Path
from unittest.mock import patch

from typer.testing import CliRunner

from {{cookiecutter.project_slug}}.main import app

runner = CliRunner()


def test_help():
    """Test that the main help command works."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Usage: " in result.output


def test_config_help():
    """Test that the config help command works."""
    result = runner.invoke(app, ["config", "--help"])
    assert result.exit_code == 0
    assert "Manage configuration settings" in result.output


class TestConfigCommand:
    """Test class for config command functionality."""
    
    def test_config_set_and_get(self):
        """Test setting and getting configuration values."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "test_config.json"
            
            with patch.dict(os.environ, {"ACLI_CONFIG_PATH": str(config_path)}):
                # Test setting a string value
                result = runner.invoke(app, ["config", "set", "test_key", "test_value"])
                assert result.exit_code == 0
                assert "Set test_key = test_value" in result.output
                
                # Test getting the value back
                result = runner.invoke(app, ["config", "get", "test_key"])
                assert result.exit_code == 0
                assert "test_key = test_value" in result.output

    def test_config_set_boolean_values(self):
        """Test setting boolean configuration values."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "test_config.json"
            
            with patch.dict(os.environ, {"ACLI_CONFIG_PATH": str(config_path)}):
                # Test setting boolean true
                result = runner.invoke(app, ["config", "set", "debug", "true"])
                assert result.exit_code == 0
                assert "Set debug = True" in result.output
                
                # Test setting boolean false
                result = runner.invoke(app, ["config", "set", "verbose", "false"])
                assert result.exit_code == 0
                assert "Set verbose = False" in result.output

    def test_config_set_numeric_values(self):
        """Test setting numeric configuration values."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "test_config.json"
            
            with patch.dict(os.environ, {"ACLI_CONFIG_PATH": str(config_path)}):
                # Test setting integer
                result = runner.invoke(app, ["config", "set", "timeout", "30"])
                assert result.exit_code == 0
                assert "Set timeout = 30" in result.output
                
                # Test setting float
                result = runner.invoke(app, ["config", "set", "threshold", "1.5"])
                assert result.exit_code == 0
                assert "Set threshold = 1.5" in result.output

    def test_config_get_missing_key(self):
        """Test getting a non-existent configuration key."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "test_config.json"
            
            with patch.dict(os.environ, {"ACLI_CONFIG_PATH": str(config_path)}):
                result = runner.invoke(app, ["config", "get", "nonexistent_key"])
                assert result.exit_code == 1
                assert "Configuration key 'nonexistent_key' not found" in result.output

    def test_config_list_empty(self):
        """Test listing configuration when no config file exists."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "test_config.json"
            
            with patch.dict(os.environ, {"ACLI_CONFIG_PATH": str(config_path)}):
                result = runner.invoke(app, ["config", "list"])
                assert result.exit_code == 0
                # Should show default configuration
                assert "Configuration Settings" in result.output

    def test_config_list_with_values(self):
        """Test listing configuration with some values set."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "test_config.json"
            
            with patch.dict(os.environ, {"ACLI_CONFIG_PATH": str(config_path)}):
                # Set some values
                runner.invoke(app, ["config", "set", "theme", "dark"])
                runner.invoke(app, ["config", "set", "debug", "true"])
                
                # List all values
                result = runner.invoke(app, ["config", "list"])
                assert result.exit_code == 0
                assert "Configuration Settings" in result.output
                assert "theme" in result.output
                assert "debug" in result.output

    def test_config_reset_cancelled(self):
        """Test cancelling configuration reset."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "test_config.json"
            
            with patch.dict(os.environ, {"ACLI_CONFIG_PATH": str(config_path)}):
                # Set a value
                runner.invoke(app, ["config", "set", "test_key", "test_value"])
                
                # Try to reset but cancel
                result = runner.invoke(app, ["config", "reset"], input="n\n")
                assert result.exit_code == 0
                assert "Reset cancelled" in result.output
                
                # Verify the value is still there
                result = runner.invoke(app, ["config", "get", "test_key"])
                assert result.exit_code == 0
                assert "test_key = test_value" in result.output

    def test_config_reset_confirmed(self):
        """Test confirming configuration reset."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "test_config.json"
            
            with patch.dict(os.environ, {"ACLI_CONFIG_PATH": str(config_path)}):
                # Set a custom value
                runner.invoke(app, ["config", "set", "custom_key", "custom_value"])
                
                # Reset configuration
                result = runner.invoke(app, ["config", "reset"], input="y\n")
                assert result.exit_code == 0
                assert "Configuration reset to defaults" in result.output
                
                # Verify custom key is gone
                result = runner.invoke(app, ["config", "get", "custom_key"])
                assert result.exit_code == 1
                
                # Verify default values are present
                result = runner.invoke(app, ["config", "get", "theme"])
                assert result.exit_code == 0
                assert "theme = default" in result.output

    def test_config_file_creation(self):
        """Test that config file is created in the right location."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "test_config.json"
            
            with patch.dict(os.environ, {"ACLI_CONFIG_PATH": str(config_path)}):
                # Set a value, which should create the file
                result = runner.invoke(app, ["config", "set", "test_key", "test_value"])
                assert result.exit_code == 0
                
                # Verify file was created
                assert config_path.exists()
                
                # Verify file content
                with open(config_path, 'r') as f:
                    config = json.load(f)
                assert config["test_key"] == "test_value"

    def test_config_corrupted_file(self):
        """Test handling of corrupted configuration file."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "test_config.json"
            
            # Create a corrupted JSON file
            with open(config_path, 'w') as f:
                f.write("{ invalid json }")
            
            with patch.dict(os.environ, {"ACLI_CONFIG_PATH": str(config_path)}):
                result = runner.invoke(app, ["config", "get", "any_key"])
                assert result.exit_code == 1
                assert "Configuration file" in result.output
                assert "corrupted" in result.output
