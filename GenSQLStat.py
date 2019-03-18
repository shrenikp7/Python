#!/usr/bin/python

####
#### Following script will read db name from dblist.txt, attatch db name to each SQL statement
#### and print SQL statement generate for each database
####

import os
import time
import datetime
import pipes
import MySQLdb
import sys

DBLIST = '/mysql/admin/scripts/dblist.txt'

if os.path.exists(DBLIST):
    file1 = open(DBLIST)
    in_file = open(DBLIST,"r")
    flength = len(in_file.readlines())
    p = 1
    dbfile = open(DBLIST,"r")
    while p <= flength:
     db = dbfile.readline()   
     db = db[:-1]        
     HOST = 'localhost'
     USER = '<id>'
     CODE = '<code>'
     SOCKET = '/data/mysql/<db_name>.sock'
     connect = MySQLdb.connect(host = HOST, user = USER, passwd = CODE, unix_socket = SOCKET)
     cursor = connect.cursor()
     sql='select TABLE_NAME from information_schema.tables where TABLE_SCHEMA=' + "'" + db + "'" + ";"
     print sql

     cursor.close()
     p= p+1
     connect.close()
    sys.exit()
    dbfile.close()
else:
   print ("Database list file not found...")
