#!/usr/bin/python3
""" takes in the name of a state as an argument and
lists all cities of that state
using the database hbtn_0e_4_usa."""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    match = sys.argv[4]
    cur.execute("""select cities.name from
                cities inner join states on states.id=cities.state_id
                where states.name like %s""", (match,))
    rows = cur.fetchall()
    temp = list(row[0] for row in rows)
    print(*temp, sep=", ")
    cur.close()
    db.close()
