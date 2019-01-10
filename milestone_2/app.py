from utils import sql_database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'u' to mark a book as unread
- 'd' to delete a book
- 'q' to quit

your choice: 
"""


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_all_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'u':
            prompt_unread_book()
        elif user_input == 'd':
            prompt_delete_book()
        user_input = input(USER_CHOICE)


def prompt_add_book():
    print("add a book")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    sql_database.add_book(title, author)

def list_all_books():
    library = sql_database.get_all_books()

    for book in library:
        read = 'YES' if book['read'] else "NO"
        print(f'Name: {book["name"]}, Author: {book["author"]}, Read: {read}')

def prompt_read_book():
    title = input("Enter Book Title: ")
    sql_database.mark_book_read(title, True)

def prompt_unread_book():
    title = input("Enter Book Title: ")
    sql_database.mark_book_read(title, False)

def prompt_delete_book():
    title = input("Enter Book Title: ")
    sql_database.delete_book(title)

menu()
