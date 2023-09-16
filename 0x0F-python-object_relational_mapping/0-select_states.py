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
	cursor = db.cursor()
	query="SELECT * FROM states ORDER BY states.id ASC"
	cursor.execute(query)
	my_states = cursor.fetchall()
	for state in my_states:
		print(state)
	cursor.close()
	db.close()
