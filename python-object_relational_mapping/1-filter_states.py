#!/usr/bin/python3
"""
script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname,
        charset="utf8"
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = cursor.fetchall()
    for state in states:
        if state[1].startswith("N"):
            print(state)
    cursor.close()
