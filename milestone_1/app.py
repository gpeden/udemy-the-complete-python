# - enter 'a' to add movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit

# - Add movies
# - See movies
# - Find a movie
# - Stop running the program

# Tasks
# []: Decide where to store movies
# []: What is the format of a movie?
# [x]: Show the user the main interface and get their input
# []: Allow user to add movies
# []: Find a movie
# [x]: Stop running the program when they type 'q'
#

movies = []


def menu():
    user_input = input("Enter 'a' to add movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies)
        elif user_input == 'f':
            find_movie()
        else:
            print("Unknown command - please try again.")

        user_input = input("Enter 'a' to add movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")


def add_movie():
    title = input("Enter Movie Title: ")
    date = input("Enter Movie Date: ")
    director = input("Enter Movie Director: ")

    movies.append(
        {
            'title': title,
            'date': date,
            'director': director
        }
    )

def show_movies(movie_list):
    for movie in movie_list:
        show_movie_details(movie)
        print()

def show_movie_details(movie):
    print(f" title:'{movie['title']}'")
    print(f" date:'{movie['date']}'")
    print(f" director:'{movie['director']}'")

def find_movie():
    find_by = input("What property are you looking for?: ")
    looking_for = input("What value are you looking for?: ")

    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])

    show_movies(found_movies)

def find_by_attribute(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)
    return found

menu()

