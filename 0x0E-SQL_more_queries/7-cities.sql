-- A script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
-- cities description:
--     id INT NOT NULL PRIMARY KEY AUTO_INCREMENT
--     state_id INT NOT NULL (should be a FK of states.id)
--     name VARCHAR(256) NOT NULL
-- if the database hbtn_0d_usa already exists, your script should not fail
-- if the table cities already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
