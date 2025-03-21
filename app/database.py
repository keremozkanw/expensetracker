import psycopg2
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import DATABASE_URL

def connect_db():
    """PostgreSQL'e bağlan ve bağlantıyı döndür"""
    conn = psycopg2.connect(DATABASE_URL)
    return conn

def create_tables():
    """Veritabanı tablolarını oluştur"""
    commands = [
        """
        CREATE TABLE IF NOT EXISTS expenses (
            id SERIAL PRIMARY KEY,
            date DATE NOT NULL,
            category VARCHAR(50) NOT NULL,
            amount NUMERIC(10, 2) NOT NULL,
            description TEXT
        )
        """
    ]

    conn = connect_db()
    cur = conn.cursor()
    for command in commands:
        cur.execute(command)
    conn.commit()
    cur.close()
    conn.close()
    print("[INFO] Veritabanı tabloları oluşturuldu.")
