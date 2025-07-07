from .core.firewall import setup as setup_firewall
from .core.ssh import harden as harden_ssh
from .core.sysctl import apply as apply_sysctl
from .core.ddos import protect as apply_ddos_protection
from .core.integrity import install as install_aide, check as check_integrity

def secure_all(ports=None):
    setup_firewall(ports)
    harden_ssh()
    apply_sysctl()
    apply_ddos_protection()
    install_aide()
