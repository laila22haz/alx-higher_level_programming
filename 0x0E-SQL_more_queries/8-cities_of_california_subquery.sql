-- lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT cities, COUNT(*)
FROM states
USE hbtn_0d_usa;
WHERE name = California
ORDER BY cities.id ASC;
