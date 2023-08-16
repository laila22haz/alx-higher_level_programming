-- lists all the cities of California that can be found in the database hbtn_0d_usa
FROM states
SELECT cities, COUNT(*)
WHERE name = California
ORDER BY cities.id ASC;
