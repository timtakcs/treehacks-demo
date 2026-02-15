import json
import sqlite3

DB_PATH = "orders.db"


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def send_notification(email: str, subject: str, body: str):
    """Placeholder for our email service."""
    print(f"Sending to {email}: {subject} — {body}")


def handle_webhook(payload: str):
    """
    Process a Stripe webhook event.

    Supports:
      - charge.failed    -> marks order as 'failed', notifies customer
      - charge.refunded  -> marks order as 'refunded', notifies customer
    """
    event = json.loads(payload)
    event_type = event["type"]
    charge = event["data"]["object"]
    charge_id = charge["id"]

    if event_type not in ("charge.failed", "charge.refunded"):
        return

    db = get_db()
    order = db.execute(
        "SELECT * FROM orders WHERE stripe_charge_id = ?", (charge_id,)
    ).fetchone()

    if order is None:
        print(f"No order found for charge {charge_id}, skipping")
        return

    new_status = "failed" if event_type == "charge.failed" else "refunded"

    db.execute(
        "UPDATE orders SET status = ? WHERE id = ?",
        (new_status, order["id"]),
    )
    db.commit()

    # Read email from the order row — no customers service round-trip
    send_notification(
        email=order["customer_email"],
        subject=f"Order {order['id']} {new_status}",
        body=f"Your order has been {new_status}. Charge: {charge_id}",
    )
