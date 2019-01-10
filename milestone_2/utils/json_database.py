
import json
LIBRARY = "library.json"


def _load_books():
    books = []
    try:
        with open(LIBRARY) as file:
            books = json.load(file)
    finally:
        return books


def add_book(name, author):
    library = _load_books()

    # don't add duplicates
    for book in library:
        if book["name"] == name:
            print(f"{name} already in library")
            return

    # add book and save
    library.append({'name': name, 'author': author, 'read': False})
    _save_books(library)


def delete_book(name):
    library = _load_books()
    library = [book for book in library if book['name'] != name]
    _save_books(library)


def get_all_books():
    return _load_books()


def mark_book_read(name, read):
    books = _load_books()

    for book in books:
        if book['name'] == name:
            book['read'] = read
            _save_books(books)
            return


def _save_books(books):
    with open(LIBRARY, "w") as file:
        json.dump(books, file)


# tests
if __name__ == "__main__":
    print(get_all_books())
    add_book("The Shining", "Stephen King")
    print(get_all_books())
    mark_book_read("The Shining", True)
    print(get_all_books())
    mark_book_read("The Shining", False)
    print(get_all_books())
    delete_book("The Shining")
    print(get_all_books())
