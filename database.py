import sqlite3
from sqlite3 import Connection

DB_NAME = "biyoti_uz.db"

def get_connection() -> Connection:
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Mahsulotlar jadvali
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL,
        images TEXT,  -- JSON formatda rasm URL yoki nomlari
        tags TEXT     -- Masalan: 'new,discount,top'
    )
    """)

    # Buyurtmalar jadvali
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_ids TEXT NOT NULL,   -- JSON formatda mahsulotlar idlari
        total_price REAL NOT NULL,
        customer_phone TEXT NOT NULL,
        order_time TEXT NOT NULL,
        status TEXT DEFAULT 'New'
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()