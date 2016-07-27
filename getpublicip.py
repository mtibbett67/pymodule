#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
NAME:
getpublicip.py

DESCRIPTION:
Makes querry to get public IP address

CREATED:
Sat Mar 21 23:21:29 2015

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

# Related third party imports
import urllib2

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

SEPARATOR = "=" * 80
NL = "\n"

# Get current public IP
CURRENT_IP = urllib2.urlopen('http://ip.42.pl/raw').read()
print NL + G + "Current IP: " + W + CURRENT_IP + NL

# Get reference IP
TXT = os.getenv("HOME") + "/pub_ip.txt"
PUB_IP = open(TXT)
PUB_IP = PUB_IP.read()
print G + "Reference IP: " + W + PUB_IP + NL

# Compare current IP to reference IP
if CURRENT_IP == PUB_IP:
    print G + "No change" + W + NL
else:
    print R + "New IP" + W + NL
    FILE = open(TXT, 'w')
    FILE.write(CURRENT_IP)
    FILE.close()
    NEW = open(TXT)
    print NEW.read()

#==============================================================================
# # Send e-mail
# import smtplib
#
# fromaddr = 'mtibbett67@gmail.com'
# toaddrs  = 'mtibbett67@gmail.com'
# msg = "Current public IP: %s" % CURRENT_IP
#
#
# # Credentials (if needed)
# username = "mtibbett67"
# print "Enter password for %s" % username
# password = raw_input(">")
#
# # The actual mail send
# server = smtplib.SMTP('smtp.gmail.com:587')
# #server = smtplib.SMTP_SSL('smtp.gmail.com:465')
# server.starttls()
# #server.login(username,password)
# server.sendmail(fromaddr, toaddrs, msg)
#server.quit()
#==============================================================================
