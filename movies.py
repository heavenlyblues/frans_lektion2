movies = ["Inception", "The Matrix", "Interstellar", "The Prestige"]
print("My previous favorite movies:", end=" ")
print(", ".join(movies))

movies.append("Memento")

for i, movie in enumerate(movies[:]):
    if movie == "The Matrix":
        movies[i] = "The Lord of the Rings"
    elif movie == "The Prestige":
        movies.remove(movie)

"""
Tried this first, but then went with the combined for loop

if "The Matrix" in movies:
    i = movies.index("The Matrix")
    movies[i] = "The Lord of the Rings"
print(movies)

if "The Prestige" in movies:
    movies.remove("The Prestige")
print(movies)

"""

movies.insert(1, "The Dark Knight")
print("My current favorite movies:", end=" ")
print(", ".join(movies))
