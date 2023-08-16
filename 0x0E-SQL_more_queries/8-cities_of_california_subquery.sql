-- lists all the cities of California that can be found in the database hbtn_0d_usa
USE hbtn_0d_usa;
SELECT id, name
FROM cities
WHERE name=
    (SELECT id
    FROM states
    WHERE name = California)
ORDER BY id ASC;
