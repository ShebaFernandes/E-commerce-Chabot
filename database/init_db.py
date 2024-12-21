import sqlite3

def create_table():
    """Create the products table if it doesn't exist."""
    try:
        with sqlite3.connect("chatbot.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price REAL NOT NULL
                )
            """)
            print("Table 'products' created or already exists.")
    except sqlite3.Error as e:
        print(f"SQLite error during table creation: {e}")

def insert_mock_data():
    """Insert mock data into the products table if it doesn't already exist."""
    try:
        with sqlite3.connect("chatbot.db") as connection:
            cursor = connection.cursor()

            cursor.execute("SELECT COUNT(*) FROM products;")
            count = cursor.fetchone()[0]

            if count == 0:
                products = [
                    ("Smartphone", 699.99), 
                    ("Laptop", 999.99), 
                    ("Headphones", 49.99),
                    ("Camera", 399.99), 
                    ("Smartwatch", 199.99), 
                    ("Book - Python", 29.99)
                ]
                cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", products)
                print("Mock data inserted successfully.")
            else:
                print(f"Table 'products' already contains {count} record(s). Skipping data insertion.")
    except sqlite3.Error as e:
        print(f"SQLite error during data insertion: {e}")

if __name__ == "__main__":
    create_table()
    insert_mock_data()
