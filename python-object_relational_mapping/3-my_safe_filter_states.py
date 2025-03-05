#!/usr/bin/python3
"""
script should take 4 arguments: mysql username,
mysql password, database name and state name searched
(safe from MySQL injection)
"""

import MySQLdb
from sys import argv, exit

if __name__ == "__main__":
    state = argv[-1]
    if any(not c.isalpha() for c in state):
        exit(1)

    try:
        database = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306,
        )

        with database.cursor() as cursor:
            query = (
                "SELECT * FROM states "
                "WHERE name LIKE BINARY '{}' "
                "ORDER BY id ASC".format(state)
            )
            cursor.execute(query)

            result = cursor.fetchall()

            if result:
                print(*result, sep="\n")

        database.close()

    except MySQLdb.OperationalError as e:
        print(f"Error connecting to the database: {e}")
