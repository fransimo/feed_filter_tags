import os
from setuptools import setup, find_packages

version = '0.1.1'

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as file:
    long_description = file.read()

# Use requirements.txt to build dependencies
with open(os.path.join(os.path.dirname(__file__), 'requirements.txt'), 'r') as file:
    required_modules = file.readlines()[1:]

setup(
    name="feed_filter_tags",
    version=version,
    packages=find_packages(exclude=('examples')),
    install_requires=required_modules,
    package_data={'': ['*.rst']},
    author="Fran Simó",
    author_email="fransimo@gmail.com",
    project_urls={
        "Source Code": "https://github.com/fransimo/feed_filter_tags",
    },
    description="Pelican feed filter to add tags",
    license="",
    keywords=["pelican", "filter"],
    url="https://github.com/fransimo/feed_filter_tags",
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
    ],
)
