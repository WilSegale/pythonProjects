import os
import mysql.connector

block_size = os.statvfs("/").f_frsize

def get_disk_space():
    total, used, free = os.statvfs("/")
    total_space = total * block_size
    used_space = (total - free) * block_size
    free_space = free * block_size
    return total_space, used_space, free_space

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Cmonster2006!@#!@#!@#",
  database="NAME_OF_DISKSPACE"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS disk_space (id INT AUTO_INCREMENT PRIMARY KEY, total_space BIGINT, used_space BIGINT, free_space BIGINT)")

total_space, used_space, free_space = get_disk_space()
sql = "INSERT INTO disk_space (total_space, used_space, free_space) VALUES (%s, %s, %s)"
val = (total_space, used_space, free_space)
mycursor.execute(sql, val)
mydb.commit()

mydb.close()
