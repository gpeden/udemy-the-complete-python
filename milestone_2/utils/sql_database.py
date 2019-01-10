from .database_connection import DatabaseConnection
from typing import List, Dict, Union

Book = Dict


def create_book_table() -> None:
    with DatabaseConnection('data.db') as db:
        cursor = db.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name TEXT primary key, author TEXT, read integer)')


def _load_books() -> List[Book]:
    with DatabaseConnection('data.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * from books");

        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

    return books


def add_book(name: str, author: str) -> None:
    with DatabaseConnection('data.db') as db:
        cursor = db.cursor()
        try:
            cursor.execute(f'INSERT INTO books VALUES(?, ?, 0)', (name, author))
        except sqlite3.IntegrityError:
            print("Skipping")
            pass


def delete_book(name: str) -> None:
    with DatabaseConnection('data.db') as db:
        cursor = db.cursor()
        cursor.execute(f'DELETE FROM books WHERE name=?', (name,))


def get_all_books() -> List[Book]:
    return _load_books()


def mark_book_read(name: str, read: int) -> None:
    with DatabaseConnection('data.db') as db:
        cursor = db.cursor()
        if read:
            cursor.execute(f'UPDATE books SET read=1 WHERE name=?', (name,))
        else:
            cursor.execute(f'UPDATE books SET read=0 WHERE name=?', (name,))

create_book_table()


# tests
if __name__ == "__main__":
    create_book_table()
    print(get_all_books())
    add_book("The Shining", "Stephen King")
    print(get_all_books())
    mark_book_read("The Shining", True)
    print(get_all_books())
    mark_book_read("The Shining", False)
    print(get_all_books())
    delete_book("The Shining")
    print(get_all_books())
