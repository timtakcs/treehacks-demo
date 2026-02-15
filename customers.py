"""
Customers service — the canonical source for customer data.

All customer fields (email, name, etc.) live here. Other services
should look up customer info by customer_id rather than storing
their own copies.
"""

import sqlite3

DB_PATH = "customers.db"


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def get_customer(customer_id: str):
    """Look up a customer by id. Returns the full customer row."""
    db = get_db()
    return db.execute(
        "SELECT * FROM customers WHERE customer_id = ?", (customer_id,)
    ).fetchone()


def get_customer_email(customer_id: str) -> str | None:
    """Convenience method — fetch just the email for a customer."""
    customer = get_customer(customer_id)
    return customer["email"] if customer else None
