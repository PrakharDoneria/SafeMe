from .utils import run, apt_install

def install():
    apt_install("aide")
    run("aideinit")
    run("cp /var/lib/aide/aide.db.new /var/lib/aide/aide.db")

def check():
    run("aide --check")