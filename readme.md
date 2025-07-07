# 🛡️ SafeMe

**SafeMe** is a one-command Linux server security tool that automates critical hardening tasks such as setting up firewalls, securing SSH access, mitigating DDoS attacks, monitoring file integrity, and locking down kernel-level network configurations — all via a simple CLI or Python API.

---

# Motivate maintainer

[![UPI](https://img.shields.io/badge/UPI-009688?style=for-the-badge&logo=upi&logoColor=white)](upi://pay?pa=prakhardoneria@upi&pn=Prakhar%20Doneria)
[![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/prakhardoneria)

## ✅ Features

* 🔐 Harden SSH server (disables root login and password-based auth)
* ⚙️ UFW firewall with configurable open ports
* 🧱 Secure kernel parameters via `sysctl`
* 🔥 Basic DDoS protection using `iptables` (rate limiting, connection limiting)
* 🧬 Monitor file integrity using `aide`
* 🧩 Designed as both a **CLI tool** and **importable Python module**
* ⚡ Runs fast and enforces security persistently across reboots

---

## 💾 Installation

```bash
pip install safeme
```

> Requires `sudo` access and tested only on Debian/Ubuntu-based systems.

---

## 🚀 Quick Start (CLI)

Run all security modules with one command:

```bash
sudo safeme secure --ports 22,443,8000
```

### What this does:

* Enables UFW and opens only ports `22`, `443`, and `8000`
* Disables root login and password authentication for SSH
* Applies kernel security policies via `/etc/sysctl.d/`
* Adds rate limiting and connection throttling via `iptables`
* Installs and initializes AIDE for file integrity monitoring

---

## 🔧 CLI Commands (Full Reference)

| Command             | Usage Example                           | Description                                                                 |
| ------------------- | --------------------------------------- | --------------------------------------------------------------------------- |
| `secure`            | `sudo safeme secure --ports 22,443`     | Run all hardening modules (firewall, SSH, sysctl, DDoS, integrity)          |
| `setup-firewall`    | `sudo safeme setup-firewall --ports 22` | Set up UFW with specified allowed ports; everything else is blocked         |
| `harden-ssh`        | `sudo safeme harden-ssh`                | Disables root login and password auth in `/etc/ssh/sshd_config`             |
| `apply-sysctl`      | `sudo safeme apply-sysctl`              | Adds safe networking defaults via `sysctl`, e.g., disables source routing   |
| `lavawall`          | `sudo safeme lavawall`                  | Adds `iptables` rules to limit incoming connections and protect against DoS |
| `install-integrity` | `sudo safeme install-integrity`         | Installs AIDE and initializes its file DB for integrity monitoring          |
| `integrity`         | `sudo safeme integrity`                 | Runs a file integrity scan using AIDE                                       |

> Use `--help` after any command to see detailed usage.

---

## 🐍 Python Usage

SafeMe can also be used programmatically in any Python automation or deployment script.

### Secure the system with all protections:

```python
from safeme import api

api.secure_all(ports=[22, 443, 8000])
```

### Use individual modules:

```python
from safeme.core.firewall import setup as setup_firewall
from safeme.core.ssh import harden as harden_ssh
from safeme.core.sysctl import apply as apply_sysctl
from safeme.core.ddos import protect as ddos_protect
from safeme.core.integrity import install as install_aide, check as run_integrity

setup_firewall([22, 443])
harden_ssh()
apply_sysctl()
ddos_protect()
install_aide()
run_integrity()
```

---

## 🖥 System Requirements

* Python 3.7 or later
* `sudo` or root privileges
* Debian/Ubuntu Linux
* System packages installed:

  ```bash
  sudo apt install -y ufw iptables-persistent aide openssh-server
  ```

---

## 📌 Notes

* All configurations are persistent across reboots
* Best used on freshly provisioned servers
* You can run each command independently without conflicts
* More modular features and hardening profiles coming soon

---

## 📄 License

**MIT License**
© 2025 [Prakhar Doneria](https://github.com/prakhardoneria)