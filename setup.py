#!/usr/bin/env python3

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os
import sys

import libgrabsite

install_requires = [
    "click>=8.0.0",
    "wpull @ https://github.com/ArchiveTeam/ludios_wpull/archive/refs/tags/5.0.3.zip",
    "lmdb>=1.7.0",
    "autobahn>=20.0.0",
    "google-re2>=1.1.0",
    "websockets>=10.0.0",
]

setup(
    name="grab-site",
    version=libgrabsite.__version__,
    description="The archivist's web crawler: WARC output, dashboard for all crawls, dynamic ignore patterns",
    url="https://ludios.org/grab-site/",
    author="Ivan Kozik",
    author_email="ivan@ludios.org",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP",
    ],
    scripts=["grab-site", "gs-server", "gs-dump-urls"],
    packages=["libgrabsite"],
    package_data={"libgrabsite": ["*.html", "*.ico", "*.txt", "ignore_sets/*"]},
    install_requires=install_requires,
)
