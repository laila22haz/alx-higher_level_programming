-- number of records with the same score in the table
SELECT COUNT(*) AS number
FROM second_table
GROUP BY score;
