#!/usr/bin/python3
"""
 A script that takes in an argument and displays
 all values in the states table of hbtn_0e_0_usa
 where name matches the argument
 """


import MySQLdb
from sys import argv


if __name__ == "__main__":

    # Connecting to the MySQL database
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cur = db.cursor()  # Using the cursor method to hold the environment
    cur.execute(
            """SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC""".format(argv[4])
            )  # Executing the query
    rows = cur.fetchall()  # Fetching all rows
    for row in rows:
        if row[1][0] == 'N':
            print(row)

    cur.close()
    db.close()
