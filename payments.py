import sqlite3
import stripe

stripe.api_version = "2018-02-06"

DB_PATH = "orders.db"


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def create_order(customer_id: str, customer_email: str, amount: int, currency: str = "usd"):
    db = get_db()
    cursor = db.execute(
        """
        INSERT INTO orders (customer_id, customer_email, amount, currency, status)
        VALUES (?, ?, ?, ?, 'pending')
        """,
        (customer_id, customer_email, amount, currency),
    )
    db.commit()
    order_id = cursor.lastrowid
    return order_id


def process_payment(order_id: int):
    db = get_db()
    order = db.execute("SELECT * FROM orders WHERE id = ?", (order_id,)).fetchone()

    if order is None:
        raise ValueError(f"Order {order_id} not found")

    if order["status"] != "pending":
        raise ValueError(f"Order {order_id} is already {order['status']}")

    # Legacy Charges API — receipt_email comes from the denormalized column
    charge = stripe.Charge.create(
        amount=order["amount"],
        currency=order["currency"],
        source="tok_visa",  # in production this comes from the frontend
        receipt_email=order["customer_email"],
        metadata={"order_id": str(order_id)},
    )

    db.execute(
        "UPDATE orders SET stripe_charge_id = ?, status = 'paid' WHERE id = ?",
        (charge.id, order_id),
    )
    db.commit()
    return charge.id
