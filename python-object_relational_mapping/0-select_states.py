#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb


if __name__ == "__main__":
    # Get MySQL connection parameters from command line arguments.
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              .format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Database connection
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create cursor object to execute queries
    cursor = db.cursor()

    # Execute SELECT query to get all states, ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all states
    states = cursor.fetchall()

    # Display results
    for state in states:
        print(state)

    # Close cursor and database
    cursor.close()
    db.close()
