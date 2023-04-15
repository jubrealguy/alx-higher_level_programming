#!/usr/bin/python3
"""
 A script that lists all states from the database hbtn_0e_0_usa
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
    sql_query = """SELECT cities.name FROM cities
            INNER JOIN states ON states.id = cities.state_id
            WHERE states.name LIKE %s
            ORDER BY cities.id ASC;"""
    cur.execute(sql_query, (argv[4], ))  # Executing the query
    rows = cur.fetchall()  # Fetching all rows
    _list = []
    for row in rows:
        string = ""
        for item in row:
            string = string + item
        _list.append(string)
    print(str(_list))

    cur.close()
    db.close()
