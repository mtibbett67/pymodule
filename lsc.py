#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
NAME: lsc.py

DESCRIPTION: Get a list os scripts categorized and sorted

CREATED: Sun Apr  5 22:45:36 2015

VERSION: 0.1

AUTHOR: Mark Tibbett

AUTHOR_EMAIL: mtibbett67@gmail.com

URL: URL to get it at.

DOWNLOAD_URL: Where to download it.

INSTALL_REQUIRES: [nose]

PACKAGES: [NAME]

SCRIPTS: []
"""

# Standard library imports
import os

# Related third party imports


# Local application/library specific imports


# Clear the terminal
os.system('clear')

SEPARATOR = "=" * 80
NL = "\n"

PYHEAD = "Python scripts available"
PYLIST = os.listdir("/home/mark/Projects")

SHHEAD = "Shell scripts available"
SHLIST = os.listdir("/home/mark/Scripts")


def script_list(head, items):
    """Get list of scrips in directory"""
    print head
    print SEPARATOR
    for item in sorted(items):
        print item

    print NL

script_list(PYHEAD, PYLIST)

script_list(SHHEAD, SHLIST)
