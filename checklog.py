#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
NAME:
checklog.py

DESCRIPTION:
This script checks the tail of the log file and lists the disk space

CREATED:
Sun Mar 15 22:53:54 2015

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

'''

# Standard library imports
import os
import sys
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

# Section formats
SEPARATOR = B + '=' * 80 + W
NL = '\n'

# Clear the terminal
os.system('clear')

# Check for root or sudo.  Remove if not needed.
UID = os.getuid()

if UID != 0:
    print R + ' [!]' + O + ' ERROR:' + G + ' sysupdate' + O + \
    ' must be run as ' + R + 'root' + W
#    print R + ' [!]' + O + ' login as root (' + W + 'su root' + O + ') \
#    or try ' + W + 'sudo ./wifite.py' + W

    os.execvp('sudo', ['sudo'] + sys.argv)

else:
    print NL
    print G + 'You are running this script as ' + R + 'root' + W
    print NL + SEPARATOR + NL

    LOG = ['tail', '/var/log/messages']
    DISK = ['df', '-h']

    def check(arg1, arg2):
        '''Call subprocess to check logs'''
        print G + arg1 + W + NL
        item = subprocess.check_output(arg2)
        #subprocess.call(arg2)
        print item + NL + SEPARATOR + NL

    check('Runing tail on messages', LOG)
    check('Disk usage', DISK)
    
