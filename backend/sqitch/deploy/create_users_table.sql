-- Deploy test_landing_page:create_users_table to pg

BEGIN;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE
);

CREATE INDEX idx_users_name ON users(name);

COMMIT;
