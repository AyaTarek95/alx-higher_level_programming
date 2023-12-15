#!/usr/bin/python3
"""Take in an argument and display the values in the states table
of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("select * from states where name like binary '{}'"
                .format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
