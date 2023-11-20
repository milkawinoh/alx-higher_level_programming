#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.Connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )
    cursor = db.cursor()
    cursor.execute("SELECT DISTINCT * FROM states ORDER BY states.id ASC")

    rows = cursor.fetchall()
    for i in rows:
        print(i)
    cursor.close()
    db.close()
