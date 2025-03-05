#!/usr/bin/python3
"""
script should take 4 arguments: mysql username,
mysql password, database name and state name.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    MYSQL_USERNAME = sys.argv[1]
    MYSQL_PASSWORD = sys.argv[2]
    DATABASE_NAME = sys.argv[3]
    STATE_NAME = sys.argv[4]

    database = MySQLdb.connect(
        host="localhost",
        user=MYSQL_USERNAME,
        passwd=MYSQL_PASSWORD,
        db=DATABASE_NAME,
        port=3306,
    )

    cursor = database.cursor()

    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (STATE_NAME,))

    cities = cursor.fetchall()

    city_names = [city[0] for city in cities]
    print(", ".join(city_names))

    cursor.close()
    database.close()
