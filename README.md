# A cookiecutter to bake tasty Python Typer CLI tools :cookie:

![Come to the dark side... We have cookies!](https://raw.githubusercontent.com/ltpitt/python-cookiecutter-typer-cli/master/darth_vader_cookies.jpg)

## Comes with:

- [x] Containerization
- [x] Pre-commit hooks
- [x] Dependabot configuration
- [x] typer
- [x] rich
- [x] shellingham
- [x] mypy
- [x] black
- [x] flake8
- [x] mkdocs-material
- [x] packaging

## Usage

Install cookiecutter.

```bash
pip install --user cookiecutter
```

Generate your project template using cookiecutter.

```bash
cookiecutter gh:ltpitt/python-cookiecutter-typer-cli
```

## Project Setup

1. `cd` into project directory.

2. Create a virtual environment.

```bash
python -m venv venv
```

3. Linux / Mac - Activate it.

```bash
source venv/Scripts/activate
```

3. Windows - Activate it.

```bash
source venv/Scripts/Activate.ps1
```

4. Linux / Mac - Install development dependencies with editable mode to test the CLI.

```bash
make install
```

4. Windows - Install development dependencies with editable mode to test the CLI.

```bash
pip install -e . -r requirements/dev.txt
```

## Take your CLI for a spin

This Cookiecutter comes with two generic CLI commands, namely, `items` and `users`.

> **NOTE**
>
> `<<cli_command>>` is the executable command you choose for your CLI during project setup.

```bash
<<cli_command>> items
```

```bash
<<cli_command>> users
```

### Test with Docker

CLI commands can be tested with Docker.

1. Build an image for the CLI.

   Image is tagged <<cli_command>> name.

```bash
make docker-image
```

2. Run the command inside the container.

```bash
docker-run --rm <<cli_command>> --help
```

## Documentation

1. Linux / Mac - Install documentation-related dependencies.

```bash
make docs
```

1. Windows - Install development dependencies with editable mode to test the CLI.

```bash
pip install -r requirements/docs.txt
```

2. Linux / Mac - Serve the docs locally.

```bash
make serve-docs
```

2. Windows - Serve the docs locally.

```bash
mkdocs serve -f docs/mkdocs.yml
```

## Linux / Mac - Distribution

> **NOTE**
>
> Make sure you have account in [PyPI](https://pypi.org/account/register/) before you try this out.

To publish you CLI to PyPI, run:

```bash
make distributions
```

`dist` directory will be created inside your project directory. Upload it to PyPI using:

```bash
twine dist/*
```

## Linux / Mac - Help

For help related to make commands.

```bash
make help
```
