####
#### This is Python basic script to take dump of MySQL table with condition / dump selected partition of the table.
#### Intereseting item is to notice escape "\" to tell Python interpreter how to interpret double quote " and get into command line
####

#!/usr/bin/python
import os

USER='<id>'
CODE='<code>'
SOCKET='/mysql/mysql.sock'
DB1='<db_name>'
TABLE1='<table_1>'
TABLE2='<table_2>'
DUMPFILE1='/mysql/dump/<FileName>.sql'
DUMPFILE2='/mysql/dump/<FileName>.sql'
CONDITION="<Date> between '20201001000000' and '20201101000000'"

dumpdb1 = "mysqldump" + " " + "-u" + USER +" " +  "-p" + CODE + " " + "-S" + SOCKET + " " +  DB1 + " " + TABLE1 +" " + "--where=" +"\""+ CONDITION +"\"" ">" +" " + DUMPFILE1
os.system(dumpdb1)

dumpdb2 = "mysqldump" + " " + "-u" + USER +" " +  "-p" + CODE + " " + "-S" + SOCKET + " " +  DB1 + " " + TABLE2 +" " + "--where=" +"\""+ CONDITION +"\"" ">" +" " + DUMPFILE2
os.system(dumpdb2)
