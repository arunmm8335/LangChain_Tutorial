from pathlib import Path
import sqlite3


db_path = Path(__file__).resolve().parent / "SalesDB" / "sales.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT id, product_name, category, quantity, price FROM sales")
rows = cursor.fetchall()

for row in rows:
	print(row)

cursor.close()
conn.close()
