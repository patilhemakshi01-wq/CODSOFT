# Simple Recommendation System

movies = {
    "action": ["Avengers", "Batman", "John Wick"],
    "romance": ["Titanic", "The Notebook", "Me Before You"],
    "comedy": ["Hera Pheri", "3 Idiots", "Dhamaal"],
    "horror": ["Conjuring", "Annabelle", "It"]
}

def recommend():
    print("Movie Recommendation System")
    print("Available genres:", ", ".join(movies.keys()))

    choice = input("Enter a genre: ").lower()

    if choice in movies:
        print("Recommended movies:")
        for movie in movies[choice]:
            print("-", movie)
    else:
        print("Sorry! Genre not found.")

recommend()
