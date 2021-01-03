#!/usr/bin/python

import setuptools

with open("./dnstap_pb/__init__.py", "r") as fh:
    for line in fh.read().splitlines():
        if line.startswith('__version__'):
            PKG_VERSION = line.split('"')[1]
            
with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
    
KEYWORDS = ('dnstap protobuf decoder encoder')

setuptools.setup(
    name="dnstap_pb",
    version=PKG_VERSION,
    author="Denis MACHARD",
    author_email="d.machard@gmail.com",
    description="Dnstap Protocol Buffers implementation in Python",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/dmachard/python-dnstap-protobuf",
    packages=['dnstap_pb'],
    include_package_data=True,
    platforms='any',
    keywords=KEYWORDS,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
    ],
    install_requires=[
        "protobuf"
    ]
)
