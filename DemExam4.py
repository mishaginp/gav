from DemExam3 import window_edit
import psycopg2
from psycopg2 import sql


def view_partner(name=None):
    conn = None
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="1111",
            host="localhost",
            port="5432"
        )
        print("Подключение установлено")

        cursor = conn.cursor()

        if name:
            # Безопасный параметризованный запрос
            cursor.execute(
                """SELECT type, name, director, email, phone_num, adres, rating 
                   FROM partners 
                   WHERE name = %s 
                   ORDER BY name""",
                (name,)
            )
            result = cursor.fetchone()
            if result:
                print(result)
                window_edit(result)
            else:
                print(f"Партнёр с именем '{name}' не найден.")
                window_edit()  # или вызов без данных, если нужно
        else:
            window_edit()


    except psycopg2.Error as e:
        print(f"Ошибка при работе с PostgreSQL: {e}")
    finally:
        if conn:
            conn.close()
            print("Подключение закрыто")


if __name__ == "__main__":
    view_partner("Паркет 29")

if __name__ == "__main__":
    view_partner("Паркет 29")