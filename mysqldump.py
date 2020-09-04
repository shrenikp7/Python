#!/usr/bin/python
import os

USER='<id>'
CODE='<code>'
SOCKET='<socket>'
DB1='<db_name>'
TABLE1='<table_name1>'
TABLE2='<table_name2>'
DUMPFILE1='/tmp/<schema.tab_name>.sql'
DUMPFILE2='/tmp/<schema.tab2_name>.sql''

dumpdb1 = "mysqldump" + " " + "-u" + USER +" " +  "-p" + CODE + " " + "-S" + SOCKET + " " +  DB1 + " " + TABLE1 + " " + ">" +" " + DUMPFILE1
os.system(dumpdb1)

dumpdb2 = "mysqldump" + " " + "-u" + USER +" " +  "-p" + CODE + " " + "-S" + SOCKET + " " +  DB1 + " " + TABLE2 + " " + ">" +" " + DUMPFILE2
os.system(dumpdb2)
