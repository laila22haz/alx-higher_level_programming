-- number of records with the same score in the table
SELECT COUNT(score) AS number
FROM first_table
GROUP BY score;
