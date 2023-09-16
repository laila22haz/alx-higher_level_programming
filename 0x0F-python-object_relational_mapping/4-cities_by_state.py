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
    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities \
        INNER JOIN states ON cities.state_id = states.id\
        ORDER BY cities.id ASC"
    cursor.execute(query)
    my_city = cursor.fetchall()
    for city in my_city:
        print(city)
    cursor.close()
    db.close()
