#!/usr/bin/env python

import os, sys


def heart():
    os.system("msfconsole -q -r ./check/vuln/heartburn/rs")
    sys.exit()

def execute():
    heart()

__all__ = ['heart', 'execute']
