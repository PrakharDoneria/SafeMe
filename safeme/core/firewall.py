from .utils import run, apt_install

def setup(ports=None):
    apt_install("ufw")
    run("ufw default deny incoming")
    run("ufw default allow outgoing")
    ports = ports or [22, 80, 443]
    for port in ports:
        run(f"ufw allow {port}")
    run("ufw --force enable")
