DROP TABLE artists;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

-- INSERT INTO artists (first_name, last_name) VALUES ("Eva", "Cassidy");