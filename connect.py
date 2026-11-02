# connect.py
import psycopg2
from config import DB_CONFIG


def get_connection():
    """Возвращает новое подключение к PostgreSQL."""
    return psycopg2.connect(**DB_CONFIG)


def create_tables():
    """Создаёт таблицы, если их ещё нет."""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS contacts (
                    id         SERIAL PRIMARY KEY,
                    first_name VARCHAR(100) NOT NULL,
                    last_name  VARCHAR(100) NOT NULL,
                    phone      VARCHAR(20)  NOT NULL UNIQUE
                );
            """)
        conn.commit()