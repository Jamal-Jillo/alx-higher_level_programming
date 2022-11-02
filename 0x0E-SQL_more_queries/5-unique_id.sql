-- A script that creates the table unique_id on your MySQL server.
-- unique_id description:
--    id INT with the default value 1 and must be unique
--    name VARCHAR(256)
-- if the table unique_id already exists, your script should not fail
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
