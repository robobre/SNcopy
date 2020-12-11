#!/usr/bin/python
import paramiko
from scp import SCPClient
import sys, getopt

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client


try:
    opts,args=getopt.getopt(sys.argv[1:], "ht:lup", ["help","Tarball=","logFile=","username=","password="])
except getopt.GetoptError as err:
    print "error option"
    sys.exit(2)
password=none
username=none
host=none
#par=sys.argv
#data=' '.join(sys.argv[1:])
#print data
#print type(par)
for o, a in opts:
    if o in ("-h", "--help"):
        print "-h print this help"
        print "-t Tarball file <path>/<file name>"
        print "-l Log file <path>/<file name>"
        print "-h hostname of destination"
        print "-u username of remote server"
        print "-p password" 
        sys.exit()
    if o in ("-p", "--passworf")
#ssh = createSSHClient(server, port, user, password)
#scp = SCPClient(ssh.get_transport())

