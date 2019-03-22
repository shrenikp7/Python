#!/usr/bin/python

####
#### Following script read table name from DB_NAME.txt and put partition older than 90 days
#### into the file which is created at specific location. 
####

import MySQLdb
import os
import time
import datetime
import sys
import timedelta

TBLIST = '/mysql/admin/scripts/dbfiledir/DB_NAME.txt'

HOST = 'localhost'
USER = '<id>'
CODE = '<code>'
SOCKET = '/data/mysql/<db_name>.sock'

connect = MySQLdb.connect(host = HOST, user = USER, passwd = CODE, unix_socket = SOCKET)
cursor = connect.cursor()
in_file = open(TBLIST,"r")
with open(TBLIST) as f:
    content = f.readlines()
    f.close()
content = [x.strip() for x in content]

for tab in content:
    
    today = datetime.date.today().strftime("%Y%m%d")
    days_before = (datetime.datetime.today()-datetime.timedelta(days=90)).strftime("%Y%m%d%H%M%S")
    f=open('/mysql/admin/scripts/dbfiledir/tabfiledir/'+ tab +'.txt', 'w')
    sql='SELECT distinct(a.PARTITION_NAME) FROM INFORMATION_SCHEMA.PARTITIONS a, ghlpoc.CCB_SV_SVSEEK b WHERE a.TABLE_NAME=' + "'" + tab+"'" + "and" + " " + "b.ENDDATE<'"+ days_before+"'" +";"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        f.write("%s\n" % str(row [0]))
    f.close()
cursor.close()
connect.close()
sys.exit()
