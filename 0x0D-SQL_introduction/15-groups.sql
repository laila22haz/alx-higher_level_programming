-- number of records with the same score in the table
SELECT id, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY id DESC;
