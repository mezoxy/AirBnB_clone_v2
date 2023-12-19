-- Write a script that prepares a MySQL server for the project
-- Creating the database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creating the user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED WITH 'hbnb_dev_pwd';
-- GIVE THE GRANTS TO THE USER
GRANT SELECT ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
