from datetime import datetime
from app.database import connect_db

def validate_date(date_str):
    """Girilen tarihin doğru formatta olup olmadığını kontrol eder."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def format_currency(amount):
    """TL cinsinden para birimini düzgün gösterir."""
    return f"{amount:,.2f} TL".replace(",", ".")

def get_monthly_expenses(year, month):
    """Belirtilen yıl ve ay içindeki giderleri döndürür."""
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT date, category, amount, description 
        FROM expenses 
        WHERE EXTRACT(YEAR FROM date) = %s AND EXTRACT(MONTH FROM date) = %s
        ORDER BY date DESC
        """,
        (year, month)
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_total_expenses():
    """Tüm harcamaların toplamını döndürür."""
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT SUM(amount) FROM expenses")
    total = cur.fetchone()[0]
    cur.close()
    conn.close()
    return total if total else 0.0
