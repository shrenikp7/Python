#!/usr/bin/python
## Script Name : bkup_1.py Using subprocess module 
## Script Purpose: Execute full backup of the MySQL Enterprise, compress it, check status, and email backup log
## Author : Shrenik Parekh


# Import python libraries
import os
import time
import datetime
import pipes
import socket
import subprocess
import re

host = socket.gethostname()
date = time.strftime('%Y%b%d-%H%M%S')
date1 = time.strftime('%Y-%m-%d.%H-%M-%S')
backupdir="--backup-dir=/tmp/backup" + date
backupimage="--backup-image=/mysql/NFS/"+host+".<DBName>.backup.mbi_" + date
image="backup-to-image --compress"
logfile="/tmp/backup"+date+'/meta/MEB_'+date1+'.log'
mail_list="shrenik\@<Domain>.com"
message ='"mysqlbackup completed OK"'

cmd1 = "/bin/mysqlbackup" + " " + backupdir + " " + backupimage + " " + image
p1 = subprocess.Popen(cmd1, stdin=None, stdout=subprocess.PIPE, shell=True)
#### In absence of following commad for p1 will not be terminate while running script manually
result1 = p1.communicate()[0]

cmd2 = "grep -c" + ' ' + message + ' ' + logfile
p2 = subprocess.Popen(cmd2, stdin=None, stdout=subprocess.PIPE, shell=True)
result = int(p2.communicate()[0])
if result == 2:
  cmd3= "mailx -s 'MEB Backup Log ' " +  mail_list + "< "+ logfile
  p3 = subprocess.Popen(cmd3, stdin=None, stdout=subprocess.PIPE, shell=True)
else:
  cmd4="mailx -s 'MEB Backup FAILED ' " +  mail_list + "< "+ logfile
  p4 = subprocess.Popen(cmd4, stdin=None, stdout=subprocess.PIPE, shell=True)
# End of script
