# db_utils.py (или в DemExam2.py)
import psycopg2

def get_sales_history(partner_name):
    """Возвращает список продаж для партнера: [(product, quantity, sale_date), ...]"""
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="1111",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        cursor.execute("""
            SELECT product_name, quantity, sale_date 
            FROM sales 
            WHERE partner_name = %s 
            ORDER BY sale_date DESC
        """, (partner_name,))
        result = cursor.fetchall()
        conn.close()
        return result
    except Exception as e:
        print(f"Ошибка при получении истории продаж: {e}")
        return []