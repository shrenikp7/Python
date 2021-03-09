#!/usr/bin/python
## Script Name : bkup_1.py Using subprocess module, check exist status using wait
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
backupimage="--backup-image=/mysql/NFS/"+host+".<DB_Name>.backup.mbi_" + date
image="backup-to-image --compress"
logfile="/tmp/backup"+date+'/meta/MEB_'+date1+'.log'
mail_list="shrenik\@<Domain>.com"
message ='"mysqlbackup completed OK"'

cmd1 = "/bin/mysqlbackup" + " " + backupdir + " " + backupimage + " " + image
p1 = subprocess.Popen(cmd1, stdin=None, stdout=subprocess.PIPE, shell=True)
#### Check the staut of the p1 execution, success status is 0
exit_code = p1.wait()
if exit_code != 0:
  cm1 = "mailx -s 'MEB Backup command fail ' " +  mail_list + "< "+ logfile
  pexit = subprocess.Popen(cm1, stdin=None, stdout=subprocess.PIPE, shell=True)
else:
 print "MEB backup command works"

cmd2 = "grep -c" + ' ' + message + ' ' + logfile
p2 = subprocess.Popen(cmd2, stdin=None, stdout=subprocess.PIPE, shell=True)
result = int(p2.communicate()[0])
if result == 2:
  cmd3= "mailx -s 'MEB Full Backup Log ' " +  mail_list + "< "+ logfile
  p3 = subprocess.Popen(cmd3, stdin=None, stdout=subprocess.PIPE, shell=True)
else:
  cmd4="mailx -s 'MEB Backup FAILED ' " +  mail_list + "< "+ logfile
  p4 = subprocess.Popen(cmd4, stdin=None, stdout=subprocess.PIPE, shell=True)
# End of script
