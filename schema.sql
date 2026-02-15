CREATE TABLE IF NOT EXISTS orders (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id     TEXT    NOT NULL,
    customer_email  TEXT    NOT NULL,
    amount          INTEGER NOT NULL,  -- in cents
    currency        TEXT    NOT NULL DEFAULT 'usd',
    stripe_charge_id TEXT,
    status          TEXT    NOT NULL DEFAULT 'pending',
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
