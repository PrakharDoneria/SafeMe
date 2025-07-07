from setuptools import setup, find_packages
from pathlib import Path

this_dir = Path(__file__).parent
long_description = (this_dir / "readme.md").read_text(encoding="utf-8")

setup(
    name="SafeMe",
    version="0.1.3",
    description="One-command backend Linux server security: firewall, SSH hardening, DDoS protection, integrity checks and more.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Prakhar Doneria",
    author_email="prakhardoneria3@gmail.com",
    url="https://github.com/prakhardoneria/safeme",
    project_urls={
        "Homepage": "https://github.com/prakhardoneria/safeme",
        "Repository": "https://github.com/prakhardoneria/safeme",
        "Issues": "https://github.com/prakhardoneria/safeme/issues",
    },
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "typer[all]",
    ],
    entry_points={
        "console_scripts": [
            "safeme = safeme.cli:app",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)
