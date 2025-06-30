import sqlite3

conn = sqlite3.connect('store.db')
conn.execute('DROP TABLE IF EXISTS products')
conn.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    category TEXT NOT NULL,
    description TEXT,
    image TEXT
)
""")

products = [
    ('Classic Denim Jacket', 79.99, 'Jackets', 'Trendy denim jacket with a snug fit.', 'ClassicDenimJacket.jpg'),
    ('Floral Summer Dress', 49.99, 'Dresses', 'Lightweight and colorful summer dress.', 'FloralSummerDress.jpg'),
    ('Running Sneakers', 99.99, 'Shoes', 'Durable sneakers for everyday wear.', 'RunningSneakers.jpg')
]

conn.executemany("INSERT INTO products (name, price, category, description, image) VALUES (?, ?, ?, ?, ?)", products)
conn.commit()
conn.close()

print("✅ Database created and seeded successfully.")
