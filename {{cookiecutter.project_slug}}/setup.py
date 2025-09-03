"""Package setup"""
import setuptools


with open("README.md", "r") as f:
    long_description = f.read()

requirements = ["typer>=0.17.0", "rich>=14.0.0", "shellingham>=1.5.0", "requests>=2.32.0"]


setuptools.setup(
    name="{{cookiecutter.project_slug}}",
    version="0.0.1",
    author="{{cookiecutter.author}}",
    description="{{cookiecutter.description}}",
    packages=setuptools.find_packages(
        exclude=["dist", "build", "*.egg-info", "tests"]
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "{{cookiecutter.cli_command.strip().lower().replace(' ', '_').replace('-', '_')}} = {{cookiecutter.project_slug}}.main:{{cookiecutter.cli_command}}"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
)
