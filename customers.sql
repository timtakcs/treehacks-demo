CREATE TABLE IF NOT EXISTS customers (
    customer_id     TEXT    PRIMARY KEY,
    email           TEXT    NOT NULL UNIQUE,
    name            TEXT    NOT NULL,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
