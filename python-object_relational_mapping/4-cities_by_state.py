#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0c_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON states.id=cities.states_id""")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
