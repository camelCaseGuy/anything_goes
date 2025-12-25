import sqlite3

conn = sqlite3.connect("sandbox.db")
cur = conn.cursor()

# Create example tables
cur.executescript("""
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS orders;

CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    country TEXT
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INT,
    amount REAL,
    order_date TEXT
);
""")

# Insert rows
cur.executemany(
    "INSERT INTO customers VALUES (?, ?, ?)",
    [
        (1, "Alice", "USA"),
        (2, "Bob", "USA"),
        (3, "Carlos", "Mexico"),
        (4, "Dieter", "Germany"),
    ]
)

cur.executemany(
    "INSERT INTO orders VALUES (?, ?, ?, ?)",
    [
        (1, 1, 120.0, "2024-01-01"),
        (2, 1, 50.0, "2024-01-02"),
        (3, 2, 80.0, "2024-01-03"),
        (4, 4, 200.0, "2024-01-06"),
    ]
)

conn.commit()
print("Database ready: sandbox.db")
