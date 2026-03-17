from pathlib import Path
import sqlite3

db_dir = Path(__file__).resolve().parent / "SalesDB"
db_dir.mkdir(exist_ok=True)

conn = sqlite3.connect(db_dir / "sales.db")
cursor = conn.cursor()
cursor.execute(
	"""
	CREATE TABLE IF NOT EXISTS sales (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		product_name TEXT NOT NULL,
		category TEXT NOT NULL,
		quantity INTEGER NOT NULL,
		price REAL NOT NULL
	)
	"""
)

cursor.execute("SELECT COUNT(*) FROM sales")
row_count = cursor.fetchone()[0]

if row_count == 0:
	cursor.execute(
		"""
		INSERT INTO sales (product_name, category, quantity, price)
		VALUES (?, ?, ?, ?)
		""",
		("Laptop", "Electronics", 5, 75000.0),
	)
	cursor.execute(
		"""
		INSERT INTO sales (product_name, category, quantity, price)
		VALUES (?, ?, ?, ?)
		""",
		("Mouse", "Electronics", 20, 1200.0),
	)
	cursor.execute(
		"""
		INSERT INTO sales (product_name, category, quantity, price)
		VALUES (?, ?, ?, ?)
		""",
		("Office Chair", "Furniture", 8, 6500.0),
	)

conn.commit()
cursor.close()
conn.close()

print("Database initialized successfully.")
  