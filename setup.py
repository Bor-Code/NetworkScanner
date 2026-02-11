from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="network-scanner-pro",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Professional cross-platform network scanner with modern GUI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/NetworkScanner",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Networking",
    ],
    python_requires=">=3.8",
    install_requires=[
        "scapy>=2.5.0",
        "colorama>=0.4.6",
        "pyyaml>=6.0",
        "python-nmap>=0.7.1",
    ],
    entry_points={
        "console_scripts": [
            "netscan=src.main:main",
            "netscan-gui=app:main",
        ],
    },
    include_package_data=True,
)
