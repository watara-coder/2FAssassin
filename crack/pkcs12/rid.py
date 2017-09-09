#!/usr/bin/env python

import os, sys, re
from glob import glob
from classes.Colour import Colour
import subprocess
from subprocess import Popen
from crack.pkcs12 import win
import os.path

def median():
    _file= "/root/2fassassin/crack/pkcs12/crack.log"
    if ( not os.path.isfile(_file)):
        print(Colour.RED + "\n Error: Record not found. Please crack the passwords on client certificate first! \n" + Colour.END)
        win.crack()
    else:
        print(Colour.RED + "\n Record is found. Start removing the passwords from client certificate .... ...\n" + Colour.END)
        try:
            strip()
        except:
            print "\n Error: Failed to remove passwords from client certificate! \n"
            sys.exit()


def identifier():
    '''
    PASS = "cat crack.log | grep 'Password found:' | awk '{print $9}'"
    subprocess.call(PASS, shell=True);return answer
    '''
    blowjob = "cat crack.log | grep 'Password found:' | awk '{print $9}'"
    p = subprocess.Popen(blowjob, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    return output


def strip():
    answer = identifier()
    print (Colour.RED + "\n Cracked password: " + answer + Colour.END )

__all__ = ['identifier', 'strip', 'median']
