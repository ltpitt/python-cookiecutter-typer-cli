"""
Create command for the CLI.
"""
import typer

app = typer.Typer(no_args_is_help=True)


@app.command()
def create(item: str):
    print(f"Creating item: {item}")


@app.command()
def delete(item: str):
    print(f"Deleting item: {item}")


@app.command()
def sell(item: str):
    print(f"Selling item: {item}")


if __name__ == "__main__":
    app()
