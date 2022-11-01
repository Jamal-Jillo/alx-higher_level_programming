-- A script that creates a table called first_table in the current database if it does not exist.
-- first_table description:
--     id INT
--     name VARCHAR(256)
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
