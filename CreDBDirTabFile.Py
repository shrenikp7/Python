#!/usr/bin/python

####
#### Script Name - credbfile.py
#### Script Author - Shrenik Parekh
#### Purpose of this script is to read database name from file dblist.txt, create directory for each database.
#### In each database directory it will create file for each table with name DBNAME.txt and in this file 
#### it is going to store table names 
####

import MySQLdb
import os
import time
import datetime
import sys

DBLIST = '/mysql/admin/scripts/dblist.txt'

HOST = 'localhost'
USER = '<id>'
CODE = '<code>'
SOCKET = '/data/mysql/<db_name>.sock'

connect = MySQLdb.connect(host = HOST, user = USER, passwd = CODE, unix_socket = SOCKET)
cursor = connect.cursor()
in_file = open(DBLIST,"r")
with open(DBLIST) as f:
    content = f.readlines()
    f.close()
content = [x.strip() for x in content]

for db in content:
    ####
    #### Create directory for each database at /mysql/admin/scripts/dbdir/
    ####
    dirpath = "/mysql/admin/dbdir/" + db
    os.mkdir(dirpath);
    os.chdir(dirpath);
    ####
    #### Create text file DBNAME.txt having table names in each database directory
    f=open(db +'.txt', 'w')
    ####
    #### Get table names into the file 
    sql='select TABLE_NAME from information_schema.tables where TABLE_SCHEMA=' + "'" + db + "'" + ";"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        f.write("%s\n" % str(row [0]))
    f.close()
cursor.close()
connect.close()
sys.exit()
