-- creates the table unique_id
CREATE TABLE IF NOT EXISTS unique_id (
    id int DEFAULT 1 NOT NULL UNIQUE,
    name VARCHAR(256)
);