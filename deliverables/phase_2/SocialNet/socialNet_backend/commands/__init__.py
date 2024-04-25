import click

from socialNet_backend.app import config
from socialNet_backend.commands.codegen import gen_repo_code
from socialNet_backend.commands.db import db
from socialNet_backend.commands.server import run_server, run_grpc_server
from socialNet_backend.commands.seed import seed, make_user


@click.group()
def cli():
    pass


cli.add_command(db)
cli.add_command(run_server)
cli.add_command(run_grpc_server)


if not config.PRODUCTION:
    cli.add_command(gen_repo_code)
    cli.add_command(make_user)
    cli.add_command(seed)
