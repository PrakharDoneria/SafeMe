from .utils import run, apt_install

def protect():
    run("iptables -F")
    run("iptables -A INPUT -p tcp --dport 80 -m connlimit --connlimit-above 100 -j DROP")
    run("iptables -A INPUT -p tcp --dport 443 -m connlimit --connlimit-above 100 -j DROP")
    run("iptables -A INPUT -m limit --limit 25/second --limit-burst 50 -j ACCEPT")
    apt_install("iptables-persistent")
    run("netfilter-persistent save")
