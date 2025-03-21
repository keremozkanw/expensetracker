from database import connect_db

def add_expense(date, category, amount, description):
    """Gider ekleme fonksiyonu"""
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO expenses (date, category, amount, description) VALUES (%s, %s, %s, %s)",
        (date, category, amount, description),
    )
    conn.commit()
    cur.close()
    conn.close()

def list_expenses():
    """Tüm giderleri listeleme fonksiyonu"""
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses ORDER BY date DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
