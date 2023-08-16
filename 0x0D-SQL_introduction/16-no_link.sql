-- number of records with the score and name in the table
SELECT score, name COUNT(*)
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
