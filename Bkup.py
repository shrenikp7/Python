
## Script Name - bkup.py
## Script will exeuctue full backup of the MySQL Enterprise Edition using MEB - mysqlbackup
## It will backup to the image file (Backup in one file), compress it, email backup log to admin 

#!/usr/bin/python
# Import python libraries
import os
import time
import datetime
import pipes
import socket

host = socket.gethostname()
date = time.strftime('%Y%b%d-%H%M%S')
date1 = time.strftime('%Y-%m-%d.%H-%M-%S')
backupdir="--backup-dir=/tmp/backup" + date
backupimage="--backup-image=/mysql/ backup/"+host+".<db_name>.fullbkup.mbi_" + date
image="backup-to-image --compress"
#### When backup executed it will create backup log file at backup-dir destination
logfile="/tmp/backup"+date+'/meta/MEB_'+date1+'.log'
mail_list="<admin1>\@<domain>.com <admin2>\@<domain>.com <admin3>\@<domain>.com "
#### Exeucte bakcup, credential are in /etc/my.cnf file
bkupcmd = "/bin/mysqlbackup" + " " + backupdir + " " + backupimage + " " + image
os.system(bkupcmd)
#### Email backup log to admin
mailcmd = "mailx -s 'MEB Backup Log for <hostname> ' " +  mail_list + "< "+ logfile
os.system(mailcmd)
