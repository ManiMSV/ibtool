# database.py
import sqlite3
import os

DB_NAME = "users.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                sso_id TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        """)
        conn.commit()

def register_user(sso_id, password):
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (sso_id, password) VALUES (?, ?)", (sso_id, password))
            conn.commit()
            return True
    except sqlite3.IntegrityError:
        return False  # User already exists

def validate_user(sso_id, password):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE sso_id = ?", (sso_id,))
        row = cursor.fetchone()
        return row and row[0] == password
