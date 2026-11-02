# phonebook.py
import csv
import os
from connect import get_connection, create_tables


# ---------- 1. Импорт из CSV ----------
def import_from_csv(filename="contacts.csv"):
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден.")
        return

    inserted = 0
    skipped = 0
    with open(filename, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        with get_connection() as conn:
            with conn.cursor() as cur:
                for row in reader:
                    try:
                        cur.execute(
                            """INSERT INTO contacts (first_name, last_name, phone)
                               VALUES (%s, %s, %s)""",
                            (row["first_name"].strip(),
                             row["last_name"].strip(),
                             row["phone"].strip())
                        )
                        inserted += 1
                    except Exception:
                        skipped += 1
                        conn.rollback()
            conn.commit()
    print(f"Импорт завершён: добавлено {inserted}, пропущено {skipped}.")


# ---------- 2. Добавление с консоли ----------
def add_contact():
    first = input("Имя: ").strip()
    last = input("Фамилия: ").strip()
    phone = input("Телефон: ").strip()
    if not (first and last and phone):
        print("Все поля обязательны.")
        return
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """INSERT INTO contacts (first_name, last_name, phone)
                       VALUES (%s, %s, %s)""",
                    (first, last, phone)
                )
            conn.commit()
        print("Контакт добавлен.")
    except Exception as e:
        print(f"Ошибка: {e}")


# ---------- 3. Обновление ----------
def update_contact():
    phone = input("Телефон контакта, который нужно изменить: ").strip()
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, first_name, last_name FROM contacts WHERE phone = %s", (phone,))
            row = cur.fetchone()
            if not row:
                print("Контакт с таким телефоном не найден.")
                return
            cid, old_first, old_last = row
            print(f"Найден: {old_first} {old_last} ({phone})")

            new_first = input(f"Новое имя (Enter — оставить '{old_first}'): ").strip() or old_first
            new_phone = input(f"Новый телефон (Enter — оставить '{phone}'): ").strip() or phone

            cur.execute(
                "UPDATE contacts SET first_name = %s, phone = %s WHERE id = %s",
                (new_first, new_phone, cid)
            )
        conn.commit()
    print("Контакт обновлён.")


# ---------- 4. Поиск с фильтрами ----------
def search_contacts():
    print("1) По имени  2) По префиксу телефона")
    mode = input("Выбор: ").strip()

    if mode == "1":
        pattern = input("Введите часть имени: ").strip()
        sql = """SELECT first_name, last_name, phone FROM contacts
                 WHERE first_name ILIKE %s OR last_name ILIKE %s
                 ORDER BY last_name, first_name"""
        params = (f"%{pattern}%", f"%{pattern}%")
    elif mode == "2":
        prefix = input("Введите префикс телефона: ").strip()
        sql = """SELECT first_name, last_name, phone FROM contacts
                 WHERE phone LIKE %s ORDER BY last_name, first_name"""
        params = (f"{prefix}%",)
    else:
        print("Неверный выбор.")
        return

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            rows = cur.fetchall()

    if not rows:
        print("Ничего не найдено.")
    else:
        for f, l, p in rows:
            print(f"  {f} {l} — {p}")


# ---------- 5. Удаление ----------
def delete_contact():
    print("1) По имени+фамилии  2) По телефону")
    mode = input("Выбор: ").strip()

    with get_connection() as conn:
        with conn.cursor() as cur:
            if mode == "1":
                first = input("Имя: ").strip()
                last = input("Фамилия: ").strip()
                cur.execute(
                    "DELETE FROM contacts WHERE first_name = %s AND last_name = %s",
                    (first, last)
                )
            elif mode == "2":
                phone = input("Телефон: ").strip()
                cur.execute("DELETE FROM contacts WHERE phone = %s", (phone,))
            else:
                print("Неверный выбор.")
                return

            deleted = cur.rowcount
        conn.commit()
    print(f"Удалено записей: {deleted}.")


# ---------- 6. Показать все ----------
def show_all():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, first_name, last_name, phone FROM contacts ORDER BY id")
            rows = cur.fetchall()
    if not rows:
        print("Телефонная книга пуста.")
    else:
        for i, f, l, p in rows:
            print(f"  [{i}] {f} {l} — {p}")


# ---------- Меню ----------
def main():
    create_tables()
    while True:
        print("""
=== PhoneBook ===
1) Импорт из CSV
2) Добавить контакт
3) Обновить контакт
4) Поиск
5) Удалить контакт
6) Показать все
0) Выход
""")
        choice = input("Выбор: ").strip()
        if choice == "1":
            import_from_csv()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            search_contacts()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            show_all()
        elif choice == "0":
            print("Пока!")
            break
        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()