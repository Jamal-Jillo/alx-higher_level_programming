-- a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)
-- states description:
--     id INT
--     name VARCHAR(256)
--     if the database hbtn_0d_usa already exists, your script should not fail
--     if the table states already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
);
