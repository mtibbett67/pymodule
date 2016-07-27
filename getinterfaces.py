#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
NAME:
ipaddres.py

DESCRIPTION:
Get current IP address for each interface in use

CREATED:
Mon Mar 16 22:11:07 2015

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
import socket
import fcntl
import struct
import array

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
GR = '\033[37m'  # grays

# Clear the terminal
os.system('clear')

SEPARATOR = B + "=" * 80 + W
NL = "\n"


#==============================================================================
# Use those functions to enumerate all interfaces available on the system using
# Python.  Found on <http://code.activestate.com/recipes/439093/#c1>
#==============================================================================

def all_interfaces():
    """Enumerate all network interfaces"""
    max_possible = 128  # arbitrary. raise if needed.
    bytes_ = max_possible * 32
    ipv4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    names = array.array('B', '\0' * bytes_)
    outbytes = struct.unpack('iL', fcntl.ioctl(
        ipv4.fileno(),
        0x8912,  # SIOCGIFCONF
        struct.pack('iL', bytes_, names.buffer_info()[0])
    ))[0]
    namestr = names.tostring()
    lst = []
    for i in range(0, outbytes, 40):
        name = namestr[i:i+16].split('\0', 1)[0]
        ipaddress = namestr[i+20:i+24]
        lst.append((name, ipaddress))
    return lst

def format_ip(addr):
    """Format IP addresses"""
    return str(ord(addr[0])) + '.' + \
           str(ord(addr[1])) + '.' + \
           str(ord(addr[2])) + '.' + \
           str(ord(addr[3]))


IFS = all_interfaces()
for item in IFS:
    #print "%12s   %s" % (item[0], format_ip(item[1]))

    #print G + item[0] + W +"     " + format_ip(item[1])

    print G + "%8s  " % item[0] + W + format_ip(item[1])

print NL
    
