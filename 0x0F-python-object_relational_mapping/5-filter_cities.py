#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_4_usa
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
    state_name = sys.argv[4]
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities \
        INNER JOIN states ON cities.state_id = states.id\
        WHERE states.name LIKE %(state_name)s \
        ORDER BY cities.id ASC", {'state_name': state_name})
    my_city = cursor.fetchall()
    temp = (city[0] for city in my_city)
    print(", ".join(temp))
    cursor.close()
    db.close()
