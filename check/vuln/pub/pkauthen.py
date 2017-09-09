#!/usr/bin/env python

import os, re, sys
import subprocess


def check():
    os.system("bash -c 'source /root/2fassassin/check/vuln/pub/pkauth; auth'")
    filename = "/root/2fassassin/check/vuln/pub/check"
    if 'publickkey' in open(filename).read():
        print "\nRemote host supported public key authentication\n"
    else:
        print "\nRemote host do not support public key authentication\n"

__all__ = ['check']
