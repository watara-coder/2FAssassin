#!/usr/bin/env python

import os, sys
import re
from subprocess import call

def gethost():
    os.system("msfconsole -q -x 'hosts -c address -o hostess;exit'")
    os.system("grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' hostess | sort -u > host")
    filename="hostess"
    if os.path.exists(filename):
    	try:
    		os.remove(filename)
    	except OSError, e:
    		print ("Error: %s - %s." % (e.filename,e.strerror))
    else:
    	print("Sorry, the %s file could not be found." % filename)

        sys.exit()

def cgiscanner():
    os.system("nmap -p80,443 -iL host -oG - | nikto -h - | tee mapikto")
    sys.exit()

def getcgi():
    os.system("grep 'cgi-bin' mapikto | awk '{ print $3 }' | sed 's/:$//' | sort -u > targeturi")
    sys.exit()

def parsecgi():
    call (['bash', './check/vuln/shellshock/process'])
    sys.exit()

def plus():
    os.system("grep '+' /root/.msf4/loot/apache_mod_cgi_bash_env")

__all__ = ['gethost', 'cgiscanner', 'getcgi', 'parsecgi', 'plus']
