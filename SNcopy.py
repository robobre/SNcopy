#!/usr/bin/python
import paramiko
from scp import SCPClient
import sys, getopt
import getpass
import re
import os
from log_parser import metadata_parser
from database_connector import MYSQL_SIM_DATA


def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client
def progress(filename, size, sent):
    sys.stdout.write("%s\'s progress: %.2f%%   \r" % (filename, float(sent)/float(size)*100))

try:
    opts,args=getopt.getopt(sys.argv[1:], "ht:l:u:p:H:d:", ["help","Tarball=","logFile=","username=","password="])
except getopt.GetoptError as err:
    print "error option"
    sys.exit(2)
password="none"
username="none"
host="none"
tarPath="none"
logPath="none"
destPath="none"
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
        print "-d destination  path on remote server"
        sys.exit()
    if o in ("-p", "--passworf"):
        password=a
    if o in ("-t", "--TarPath"):
        tarPath=a
    if o in ("-l", "--LogFile"):
        logPath=a
    if o in ("-H", "--host"):
        host=a
    if o in ("-u", "--UserName"):
        username=a
    if o in ("-p", "--Password"):
        password=a
    if o in ("-d", "--DestPath"):
        destPath=a

#print password
print username
print host
print tarPath
print logPath
if password=="none":
    print "enter password for ssh connection:"
    password= getpass.getpass()
#print password



ssh = createSSHClient(host, 22, username, password)
scp = SCPClient(ssh.get_transport(),progress=progress)
scp.put(tarPath,destPath+"/"+os.path.basename(tarPath))

parser=metadata_parser(0)
parser.parse_file(logPath)

print parser.data
#print os.path.basename(tarPath)
myconnect=MYSQL_SIM_DATA(0)
#for comment in sys.stdin: 
#    if 'q' == comment.rstrip(): 
#        break
#    print(f'Input : {comment}') 

comment="comment"
rec1=myconnect.det_runefiles('','',os.path.basename(tarPath),'',0)
rec=myconnect.det_data(rec1,'1000-01-01',parser.data["run.run_id"],'','1000-01-01','1000-01-01',0,0,comment)
myconnect.det_ccfile( parser.data['run.run_id'],rec, '',destPath,os.path.basename(tarPath),0,'','','','1000-01-01')

