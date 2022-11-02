-- A script that creates a user user_0d_1 with the password user_0d_1_pwd
-- and grants the user all privileges
-- if the user already exists, the script should not fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
