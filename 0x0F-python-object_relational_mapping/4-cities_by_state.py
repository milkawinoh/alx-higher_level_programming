#!/usr/bin/python3
import MySQLdb
from sys import argv
"""
a script that lists all cities from the database hbtn_0e_4_usa
"""
db_connect = MySQLdb.connect(host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3])
db_cursor = db_connect.cursor()
query = """
        SELECT cities.id, cities.name, states.name 
        FROM cities
        JOIN states ON states.id = cities.state_id
        ORDER BY cities.id, states.name ASC
    """

db_cursor.execute(query)
row_selected = db_cursor.fetchall()
for row in row_selected:
    print(row)

db_connect.close()
