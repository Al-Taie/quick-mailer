#############################################
# File Name: setup.py
# Author: Ahmed Al-Taie
# Instagram: @9_Tay
# Mail: agprosup@gmail.com
# Created Time:  2020-07-26 21:41:25
#############################################

from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="altai-mailer",
    version="0.0.1",
    author="Ahmed Al-Taie",
    author_email="author@example.com",
    description="A small package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=("smtp", "mail", "gmail", "yahoo"),
    url="https://github.com/pypa/sampleproject",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
