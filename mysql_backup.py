#!/usr/bin/python
# Date : 26 Oct, 2018
# Author: Afshin Tavahin
import os
import time
import datetime
import pipes

DATABASE_HOST = 'localhost'
DATABASE_USER = 'root'
DATABASE_USER_PASSWORD = 'Your credential'
DATABASE_NAME = '/home/user/db-backup/db.txt'
BACKUP_PATH='/home/user/db-backup/'

DATETIME = time.strftime('%Y%m%d-%H%M%S')
TODATBACKUPPATH = BACKUP_PATH+ '/' + DATETIME


try:
    os.stat(TODATBACKUPPATH)
except:
    os.mkdir(TODATBACKUPPATH)

print ("Checking for database names file.")
if os.path.exists(DATABASE_NAME):
    file1 = open(DATABASE_NAME)
    multi = 1
    print("Database found!")
    print("Starting backup of all dbs listed in file " + DATABASE_NAME)
else:
    print("Database file not found")
    print("Starting backup of database " + DATABASE_NAME)
    multi = 0

if multi:
    in_file = open(DATABASE_NAME,"r")
    flength = len(in_file.readline())
    in_file.close()
    p = 1
    dbfile = open(DATABASE_NAME,"r")

    while p <= flength:
        db = dbfile.readline()
        db = db[:-1]
        dumpcmd = "mysqldump -h" + DATABASE_HOST + " -u" + DATABASE_USER + " -p" + DATABASE_USER_PASSWORD + " " + db + " > " + pipes.quote(TODATBACKUPPATH)+ "/" + db + ".sql"
        os.system(dumpcmd)
        p = p + 1
    dbfile.close()
else:
   db = DATABASE_NAME
   dumpcmd = "mysqldump -h " + DATABASE_HOST + " -u " + DATABASE_USER + " -p" + DATABASE_USER_PASSWORD + " " + db + " > " + pipes.quote(TODATBACKUPPATH) + "/" + db + ".sql"
   os.system(dumpcmd)
print ("Done.")
print ("Your backups have been created in '" + TODATBACKUPPATH + "' directory")