# app/db.py

import sqlite3

DB_FILE = \"vault.db\"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(\"\"\"
        CREATE TABLE IF NOT EXISTS vault (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT,
            username TEXT,
            password_enc TEXT
        )
    \"\"\")
    conn.commit()
    conn.close()

def save_entry(service, username, password_enc):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(\"INSERT INTO vault (service, username, password_enc) VALUES (?, ?, ?)\",
                   (service, username, password_enc))
    conn.commit()
    conn.close()

def get_entry(service):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(\"SELECT username, password_enc FROM vault WHERE service = ?\", (service,))
    row = cursor.fetchone()
    conn.close()
    return row

def delete_entry(service):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(\"DELETE FROM vault WHERE service = ?\", (service,))
    conn.commit()
    conn.close()
