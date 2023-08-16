-- creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id int AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id int NOT NULL FOREIGN KEY,
    name VARCHAR(256) NOT NULL
);
