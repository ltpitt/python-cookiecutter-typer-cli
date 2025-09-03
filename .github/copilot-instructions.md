# Python Cookiecutter Typer CLI

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

This repository contains a Cookiecutter template for generating Python CLI applications using Typer. The template creates fully-featured CLI projects with testing, documentation, Docker support, and pre-commit hooks.

## Working Effectively

### Bootstrap and Test the Cookiecutter Template
- Install cookiecutter: `pip install cookiecutter`
- Generate a test project: `cookiecutter /path/to/template --no-input`
- Navigate to generated project: `cd awesome_cli` (default project name)

### Working with Generated Projects
- Create virtual environment: `python -m venv venv`
- Activate virtual environment (Linux/Mac): `source venv/bin/activate`
- Install core dependencies: `pip install typer rich shellingham requests` -- takes 30 seconds
- **CRITICAL**: Network timeouts are common. If `make install` fails, use individual pip installs for core dependencies first
- Install additional dev dependencies individually as needed:
  - Testing: `pip install pytest` -- takes 30 seconds
  - Formatting: `pip install black` -- takes 30 seconds  
  - Documentation: `pip install mkdocs mkdocs-material mkdocs-click mkdocs-markdownextradata-plugin` -- takes 60 seconds

### Build and Test Commands
- Run tests: `pytest -vvv` or `make test` -- takes 0.3 seconds. NEVER CANCEL.
- Format code: `make format` -- takes 2 minutes for large codebases. NEVER CANCEL. Set timeout to 180+ seconds.
- Check code formatting: `make check` -- takes 5+ minutes. NEVER CANCEL. Set timeout to 600+ seconds.
- Test CLI functionality:
  - Help: `python -m awesome_cli.main --help`
  - Items: `python -m awesome_cli.main items create "test-item"`
  - Users: `python -m awesome_cli.main users create "test-user"`

### Documentation
- Start docs server: `PYTHONPATH=/path/to/project:$PYTHONPATH mkdocs serve -f docs/mkdocs.yml`
- **CRITICAL**: Documentation requires PYTHONPATH to be set to include the project directory
- Serves on http://127.0.0.1:8000/
- The generated documentation may need manual fixes for mkdocs-click compatibility with Typer

### Docker (Limited in Sandbox)
- Build image: `make docker-image` -- often fails due to network connectivity issues
- **NOTE**: Docker builds may fail in sandboxed environments due to network restrictions

## Validation

### Manual Testing Requirements
ALWAYS test generated CLI projects by running actual commands:
1. Generate a project with cookiecutter
2. Set up virtual environment and install dependencies
3. Test CLI commands: `python -m {project_name}.main --help`
4. Test subcommands: `python -m {project_name}.main items create "test"`
5. Run test suite: `pytest -vvv`
6. Test code formatting: `make format`
7. Verify documentation can be built (with PYTHONPATH set)

### Known Issues and Workarounds
- **pip install failures**: Use individual package installation instead of requirements files
- **Network timeouts**: Common in sandboxed environments - document as "fails due to network limitations"
- **Documentation errors**: mkdocs-click has compatibility issues with Typer - may need manual content updates
- **Docker build failures**: Network connectivity issues in sandboxed environments

## Common Tasks

### Repository Structure
```
.
├── README.md                           # Template usage instructions
├── cookiecutter.json                   # Template configuration
├── {{cookiecutter.project_slug}}/      # Generated project template
│   ├── Makefile                        # Build automation
│   ├── requirements/                   # Dependency definitions
│   ├── {{cookiecutter.project_slug}}/  # Main package
│   │   ├── main.py                     # CLI entry point
│   │   └── commands/                   # Command modules
│   ├── tests/                          # Test suite
│   ├── docs/                           # Documentation
│   └── Dockerfile                      # Container configuration
```

### Generated Project Commands
The generated projects include these make targets:
- `make install` -- Install dev dependencies (may fail, use manual pip install)
- `make test` -- Run pytest test suite (0.3 seconds)
- `make format` -- Format code with black (2 minutes, NEVER CANCEL)
- `make check` -- Check code formatting (5+ minutes, NEVER CANCEL)
- `make clean` -- Remove temporary files
- `make docs` -- Install documentation dependencies
- `make serve-docs` -- Serve documentation locally
- `make docker-image` -- Build Docker image (may fail in sandbox)

### Template Customization
Edit `cookiecutter.json` to change default values:
- `project_name`: Display name for the project
- `project_slug`: Package/directory name
- `cli_command`: Executable command name
- `author`: Package author
- `description`: Project description

### Testing Template Changes
1. Generate test project: `cookiecutter . --no-input`
2. Test all functionality manually as described in Validation section
3. Verify all make commands work or document known failures
4. Test CLI commands work correctly
5. Ensure documentation builds without errors

## Timing Expectations

- **NEVER CANCEL** any build or test commands
- Cookiecutter generation: 1 second
- Virtual environment creation: 5 seconds
- Core dependency installation: 30 seconds
- pytest test suite: 0.3 seconds
- Black formatting: 2 minutes (set timeout to 180+ seconds)
- Black checking: 5+ minutes (set timeout to 600+ seconds)
- Documentation server startup: 10 seconds
- Docker image build: 2+ minutes (often fails due to network)

## Notes for Developers

This is a template repository, not a regular Python project. The actual functionality is in the generated projects under `{{cookiecutter.project_slug}}/`. Always test changes by generating a new project and validating it works correctly.

When making changes to the template:
1. Modify files in `{{cookiecutter.project_slug}}/`
2. Test by generating a new project
3. Validate all commands work in the generated project
4. Update these instructions if new dependencies or steps are required