#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
NAME:
minicom.py

DESCRIPTION:
Use MiniComm to connect to a USB to Serial adapter

CREATED:
Tue Mar 17 21:51:42 2015

VERSION:
0.1

AUTHOR:
Mark Tibbett

AUTHOR_EMAIL:
mtibbett67@gmail.com

URL:
N/A

DOWNLOAD_URL:
N/A

INSTALL_REQUIRES:
[nose]

PACKAGES:
[NAME]

SCRIPTS:
[]

"""

# Standard library imports
import os
import subprocess

# Related third party imports


# Local application/library specific imports


# Clear the terminal
os.system('clear')

# Check for root or sudo.  Remove if not needed.
UID = os.getuid()

if UID != 0:

    print "This script must be run as root or sudo"

else:

    print "You are running this script as root"

    subprocess.call(["minicom", "-b 9600 -D /dev/ttyUSB0"])


