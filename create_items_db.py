import sqlite3

# データベースファイルに接続
conn = sqlite3.connect("items.db")
cursor = conn.cursor()

# itemsテーブルを作成
cursor.execute("""
CREATE TABLE items (
    item_id INTEGER PRIMARY KEY,
    item_name TEXT NOT NULL,
    price REAL NOT NULL
)
""")

# サンプルデータを挿入
sample_data = [
    (1, "Apple", 0.50),
    (2, "Banana", 0.25),
    (3, "Orange", 0.75)
]

cursor.executemany("""
INSERT INTO items (item_id, item_name, price) VALUES (?, ?, ?)
""", sample_data)

# 変更をコミットして接続を閉じる
conn.commit()
conn.close()
