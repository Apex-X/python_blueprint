from typer import Typer
from cmd import migration, serve

cli = Typer()

cli.command()(migration.migrate)
cli.command()(serve.serve)
