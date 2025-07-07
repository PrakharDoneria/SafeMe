from .utils import run

def apply():
    content = """
net.ipv4.ip_forward = 0
net.ipv4.tcp_syncookies = 1
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.default.rp_filter = 1
net.ipv4.conf.all.accept_source_route = 0
net.ipv4.conf.default.accept_source_route = 0
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.default.accept_redirects = 0
"""
    with open("/etc/sysctl.d/99-safeme.conf", "w") as f:
        f.write(content.strip())
    run("sysctl --system")