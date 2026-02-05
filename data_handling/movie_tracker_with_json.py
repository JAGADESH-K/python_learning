import json
import os

FILENAME = "movies.json"
movies = []
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
        rating = int(input("Enter you rating (1-10): "))
        if not (0 < rating > 11): raise ValueError
    except ValueError: 
        print("Enter the valid number.")
        return

    movies

    with open(FILENAME, 'w', newline='', encoding='utf-8') as f:
        json.dump({"Title": name, "Genre": genre, "Rating": f"{'⭐' * rating}"}, f, indent=2)

    return

add_movie()
print(load_movies())