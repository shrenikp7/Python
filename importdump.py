import os

USER='<id>'
CODE='<code>'
SOCKET='/mysql/mysql.sock'
DB1='<db_name1>'
DUMPFILE1='/tmp/<schema.tab1_name>.sql'
DUMPFILE2='/tmp/<schema.tab2_name>.sql'

importdump1 = "mysql" + " " + "-u" + USER +" " +  "-p" + CODE + " " + "-S" + SOCKET + " " +  DB1 + " " + "<" +" " + DUMPFILE1
os.system(importdump1)

importdump2 = "mysql" + " " + "-u" + USER +" " +  "-p" + CODE + " " + "-S" + SOCKET + " " +  DB1 + " " + "<" +" " + DUMPFILE2
os.system(importdump2)
