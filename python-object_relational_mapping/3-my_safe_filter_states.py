#!/usr/bin/env python3

"""
a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""
import MySQLdb
import sys


username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name = sys.argv[4]

db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)

cursor = db.cursor()

query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"

cursor.execute(query, (state_name,))

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
db.close()
