-- creates the database hbtn_0d_usa and the table states
CREATE DATABASE hbtn_0d_usa IF NOT EXISTS;
CREATE TABLE states IF NOT EXISTS (
    id int DEFAULT 1 NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256)
);
