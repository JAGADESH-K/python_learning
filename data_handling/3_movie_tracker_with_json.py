import json
import os

FILENAME = "movies.json"

def load_movies():
    if not os.path.exists(FILENAME): return []
    with open(FILENAME, 'r', newline='', encoding='utf-8') as f: return json.load(f)

def add_movie(movies):
    name = input("Enter the movie name: ").strip().lower()
    if any([movie['Title'].lower() == name for movie in movies]):
        print("Movie already exists")
        return
    
    genre = input("Enter the genre: ").strip().lower()

    try:
        rating = int(input("Enter your rating (1-10): "))
        if not (0 < rating < 11): raise ValueError
    except ValueError: 
        print("\nEnter the valid number.")
        return

    movies.append({'Title': name, 'Genre': genre, 'Rating': (rating * '⭐')})

    with open(FILENAME, 'w', newline='', encoding='utf-8') as f:
        json.dump(movies, f, indent=2)

    return

def view_movies(movies):
    print("\n🍿Movie Lists🍿")
    for movie in movies:
        print(f" - Title: {movie['Title']}\n - Genre: {movie['Genre']}\n - Rating: {movie['Rating']}")

def search_movie(movies):
    option = input("\nHow do you want to search?\nTo search by title enter '1'\nTo search by genre enter '2'\nTo search by rating enter '3'\nEnter your opion: ").strip()
    if option == '1' or option == '2':
        if option == '1': term = input("Enter the title: ").strip().lower()
        else: term = input("Enter the genre: ").strip().lower()

        print("\nSearch result: ")
        for movie in movies:
            if term == movie["Title"] or term == movie["Genre"]: 
                print(f" - Title: {movie['Title']}\n - Genre: {movie['Genre']}\n - Rating: {movie['Rating']}")
                return
        print("No match fount")
        return   
    
    elif option == '3':
        try:
            rating = int(input("Enter the rating: "))
            if not (0 < rating < 11): raise ValueError
        except ValueError: print("Enter the valid number")
        star_rating = '⭐' * rating

        for movie in movies:
            if star_rating == movie['Rating']:
                print(f" - Title: {movie['Title']}\n - Genre: {movie['Genre']}\n - Rating: {movie['Rating']}")
            else: print("No match fount")

        return
    
    else: 
        print("Invalid option")
        return

def run_app():
    movies = load_movies()
    while True:
        print("\n🎞️  Movie tracker applicaton 🎞️\n")
        print("Enter 1 to add a movie")
        print("Enter 2 to search for a movie")
        print("Enter 3 to view the movies")
        print("Enter 4 to exit")

        option = input("Enter an option (1-4): ").strip()

        match option:
            case '1': add_movie(movies) 
            case '2': search_movie(movies)
            case '3': view_movies(movies)
            case '4': 
                print("\nThanks for using the app 👋👋👋\n")
                break
            case _ : 
                print("Enter a valid option")
                continue

if __name__ == "__main__":
    run_app()
