#!/usr/bin/python3
"""safe from MySQL injections."""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    found = sys.argv[4]
    cur.execute("select * from states where name like %s", (found,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
