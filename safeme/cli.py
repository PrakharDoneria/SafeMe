import typer
from .api import secure_all
from .core.firewall import setup as firewall
from .core.ssh import harden as ssh
from .core.sysctl import apply as sysctl
from .core.ddos import protect as ddos_protect
from .core.integrity import install as integrity_init, check as integrity_check

app = typer.Typer()

@app.command()
def secure(ports: str = typer.Option("22,80,443", help="Allowed ports")):
    ports_list = [int(p.strip()) for p in ports.split(",")]
    secure_all(ports_list)
    typer.echo("✅ SafeMe: system hardened.")

@app.command()
def setup_firewall(ports: str = typer.Option("22,80,443")):
    firewall([int(p.strip()) for p in ports.split(",")])

@app.command()
def harden_ssh():
    ssh()

@app.command()
def apply_sysctl():
    sysctl()

@app.command()
def lavawall():
    ddos_protect()

@app.command()
def integrity():
    integrity_check()

@app.command()
def install_integrity():
    integrity_init()

if __name__ == "__main__":
    app()