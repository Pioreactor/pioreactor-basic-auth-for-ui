# -*- coding: utf-8 -*-
from __future__ import annotations

from setuptools import find_packages
from setuptools import setup

setup(
    name="pioreactor-basic-auth-for-ui",
    version="0.0.3",
    license_files=("LICENSE.txt",),
    description="Adding basic auth to the Pioreactor UI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author_email="hello@pioreactor.com",
    author="Cameron Davidson-Pilon",
    url="",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "pioreactor.plugins": "pioreactor_basic_auth_for_ui = pioreactor_basic_auth_for_ui"
    },
)
