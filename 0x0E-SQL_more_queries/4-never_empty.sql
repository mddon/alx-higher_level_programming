--creates the table id_not_null on mysql server

CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256));
