from .utils import run

def harden():
    sshd = "/etc/ssh/sshd_config"
    with open(sshd, "r") as f:
        lines = f.readlines()
    new = []
    for line in lines:
        if line.strip().startswith("PermitRootLogin"):
            new.append("PermitRootLogin no\n")
        elif line.strip().startswith("PasswordAuthentication"):
            new.append("PasswordAuthentication no\n")
        else:
            new.append(line)
    if not any("PermitRootLogin" in l for l in new):
        new.append("PermitRootLogin no\n")
    if not any("PasswordAuthentication" in l for l in new):
        new.append("PasswordAuthentication no\n")
    with open(sshd, "w") as f:
        f.writelines(new)
    run("systemctl restart sshd")
