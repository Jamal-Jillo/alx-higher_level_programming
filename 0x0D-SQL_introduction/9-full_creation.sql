-- A script that creates a table second_table in the database hbtn_0c_0 and add multiples rows.
-- Requirements:
-- -- The database name will be passed as an argument of the mysql command
-- -- If the table second_table already exists, your script should not fail
-- Description of the table second_table:
-- -- id INT
-- -- name VARCHAR(256)
-- -- score INT
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);
