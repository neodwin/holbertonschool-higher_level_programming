#!/usr/bin/python3
"""
Script should take 3 arguments: mysql username,
mysql password and database name.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Capture the command-line arguments
    MYSQL_USERNAME = sys.argv[1]
    MYSQL_PASSWORD = sys.argv[2]
    DATABASE_NAME = sys.argv[3]

    database = MySQLdb.connect(
        host="localhost",
        user=MYSQL_USERNAME,
        passwd=MYSQL_PASSWORD,
        db=DATABASE_NAME,
        port=3306,
    )

    with database.cursor() as cursor:
        cursor.execute(
            "SELECT cities.id, cities.name, states.name FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "ORDER BY cities.id ASC"
        )
        result = cursor.fetchall()
        if result:
            for row in result:
                print(row)

    database.close()
