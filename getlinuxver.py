#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
NAME:
getlinuxver

DESCRIPTION:
Get the linux version and other details

CREATED:
Mon Mar 16 21:38:58 2015

VERSION:
1.0

AUTHOR:
Mark Tibbett

AUTHOR_EMAIL:
mtibbett67@gmail.com

URL:
N/A

DOWNLOAD_URL:
N/A

INSTALL_REQUIRES:
[]

PACKAGES:
[]

SCRIPTS:
[]

"""

# Standard library imports
import os
import subprocess

# Related third party imports


# Local application/library specific imports

# Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray


# Clear the terminal
os.system('clear')

SEPARATOR = B + "=" * 80 + W
NL = "\n"

print NL
print G +"Kernel version and gcc version used to build the same" + W
print NL
FILE = open("/proc/version")
print FILE.read() + NL + SEPARATOR + NL

print G + """The lsb_release command displays certain LSB (Linux Standard Base) and
distribution-specific information""" + W
print NL
LSB_RELEASE = subprocess.check_output(["lsb_release", "-a"])
print LSB_RELEASE + NL + SEPARATOR + NL

print G + "What version of Linux (distro) you are running." + W
print NL
OS_RELEASE = open("/etc/os-release")
print OS_RELEASE.read() + NL + SEPARATOR + NL

print G + "System information" + W
print NL
def sys_inf(arg1, arg2):
    """Use subprocess to query uname values"""
    item = subprocess.check_output(["uname", arg2])
    print arg1 + item,

sys_inf("Kernel name: ", "-s")
sys_inf("Node name: ", "-n")
sys_inf("Kernel release: ", "-r")
sys_inf("Kernel version: ", "-v")
sys_inf("Machine hardware: ", "-m")
sys_inf("Processor type: ", "-p")
sys_inf("Hardware platform: ", "-i")
sys_inf("Operating system: ", "-o")
print NL #+ SEPARATOR
