import subprocess

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

def apt_install(pkg):
    run(f"apt-get install -y {pkg}")
