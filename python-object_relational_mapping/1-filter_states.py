#!/usr/bin/python3

"""a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]


db = MySQLdb.connect(host='localhost',
                     port=3306,
                     user=username,
                     passwd=password,
                     db=database)

cursor = db.cursor()

query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"

cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
db.close()
