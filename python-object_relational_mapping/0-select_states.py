#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""
from sys
import MySQLdb

if __name__ == "__main__":
    database = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )

    with database.cursor() as cursor:
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        result = cursor.fetchall()
        if result:
            print(*result, sep="\n")

    database.close()
