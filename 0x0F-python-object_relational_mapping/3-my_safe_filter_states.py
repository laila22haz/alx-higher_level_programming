#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_us
"""
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        port=3306,
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    stat_name = sys.argv[4]
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY \
                    name LIKE %(state_name)s ORDER BY \
                states.id ASC", {'state_name': stat_name})
    my_states = cursor.fetchall()
    for state in my_states:
        print(state)
    cursor.close()
    db.close()
