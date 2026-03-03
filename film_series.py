class Movie:
    def __init__(self, title, genre, year, director):
        self.title = title
        self.genre = genre
        self.year = year
        self.director = director
        self.watched = False
        self.favorite = False
        self._rating = 0

    def __str__(self):
        return f"{self.title}, {self.genre}"

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Rating must be a number")
        if value < 0 or value > 10:
            raise ValueError("Rating must be between 0 and 10")
        self._rating = value


class Collection:
    def __init__(self):
        self.movie_list = []

    def add_movie(self, movie):
        self.movie_list.append(movie)

    def remove_movie(self, movie):
        self.movie_list = [m for m in self.movie_list if m != movie]

    def mark_watched(self, movie):
        for m in self.movie_list:
            if m.title == movie:
                m.watched = True

    def mark_favorite(self, movie):
        for m in self.movie_list:
            if m.title == movie:
                m.favorite = True

    def filter_by_genre(self, genre):
        return [m for m in self.movie_list if m.genre == genre]


collection = Collection()

while True:
    print("\n--- Movie Collection Menu ---")
    print("1 - Add Movie")
    print("2 - Remove Movie")
    print("3 - Mark Movie as Watched")
    print("4 - Mark Movie as Favorite")
    print("5 - List All Movies")
    print("6 - Filter by Genre")
    print("7 - Exit")

    choice = input("Select an option: ")

    if choice == "1":
        title = input("Enter movie title: ")
        genre = input("Enter genre: ")
        year = input("Enter release year: ")
        director = input("Enter director: ")
        m = Movie(title, genre, year, director)
        collection.add_movie(m)
        print(f"{title} added to collection.")

    elif choice == "2":
        name = input("Enter movie title to remove: ")
        movie_to_remove = next((m for m in collection.movie_list if m.title == name), None)
        if movie_to_remove:
            collection.remove_movie(movie_to_remove)
            print(f"{movie_to_remove.title} removed from collection.")
        else:
            print("Movie not found!")

    elif choice == "3":
        name = input("Enter movie title to mark as watched: ")
        movie_watched = next((m for m in collection.movie_list if m.title == name), None)
        if movie_watched:
            movie_watched.watched = True
            print(f"{movie_watched.title} marked as watched.")
        else:
            print("Movie not found!")

    elif choice == "4":
        name = input("Enter movie title to mark as favorite: ")
        favorite_movie = next((m for m in collection.movie_list if m.title == name), None)
        if favorite_movie:
            favorite_movie.favorite = True
            print(f"{favorite_movie.title} added to favorites.")
        else:
            print("Movie not found!")

    elif choice == "5":
        print("\nMovies:")
        for m in collection.movie_list:
            print(f"{m} | Watched: {m.watched} | Favorite: {m.favorite} | Rating: {m.rating}")

    elif choice == "6":
        genre = input("Enter genre to filter: ")
        filtered = collection.filter_by_genre(genre)
        for m in filtered:
            print(m)

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")