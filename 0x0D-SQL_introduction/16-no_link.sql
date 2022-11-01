-- A script that lists all records of the table second_table of the database hbtn_0c_0.
-- Requirements:
-- Don't list rows without a name value
-- Results should display the score followed by the name (in this order)
-- Results should be sorted by score in descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
