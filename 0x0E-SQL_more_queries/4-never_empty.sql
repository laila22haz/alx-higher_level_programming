-- script that creates the table id_not_null
CREATE TABLE IF NOT EXISTS id_not_null (
    id = 1 int default 1,
    name VARCHAR(256) NOT NULL
);
