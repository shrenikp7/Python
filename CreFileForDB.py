#!/usr/bin/python
####
#### Following script will read db name from text file dblist.txt and create file with db name
#### with .txt exetention at specific location
####
import MySQLdb
import os
import time
import datetime
import sys

DBLIST = '/mysql/admin/scripts/dblist.txt'
QRYLIST = '/mysql/admin/scripts/tabquery.sql'

HOST = 'localhost'
USER = '<id>'
CODE = '<code>'
SOCKET = '/data/mysql/<db_name>.sock'
connect = MySQLdb.connect(host = HOST, user = USER, passwd = CODE, unix_socket = SOCKET)

cursor = connect.cursor()
file1 = open(DBLIST)
in_file = open(DBLIST,"r")
flength = len(in_file.readlines())
p = 1
dbfile = open(DBLIST,"r")
while p <= flength:
 db = dbfile.readline()  
 db = db[:-1] 
 f=open('/mysql/admin/scripts/dbfiledir/'+db+'.txt', 'w')
 f.close()
 p= p+1
cursor.close()
connect.close()
sys.exit()
