#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)
 from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user = sys.argv[1]
    else:
        print("Error: no user provided.")

db = MySQLdb.connect(host='localhost',
                     port=3306,
                     user=sys.argv[1],
                     passwd=sys.argv[2],
                     db=sys.argv[3])

cursor = db.cursor()

query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"

cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
db.close()
