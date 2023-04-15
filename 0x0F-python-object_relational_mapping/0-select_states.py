#!/usr/bin/python3
"""
 A script that lists all states from the database hbtn_0e_0_usa
 """

import MySQLdb
from sys import argv


# Connecting to the MySQL database
db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
        )
cur = db.cursor()  # Using the cursor method
cur.execute("SELECT * FROM states")  # Executing the query
rows = cur.fetchall()  # Fetching all rows
for row in rows:
    print(row)
cur.close()
db.close()
