import imdb
import random

ia = imdb.Cinemagoer()
random_movie = random.randint(0, 250)

tops = ia.get_top250_tv()
print("Tops type:", type(tops))
bottom = ia.get_bottom100_movies()

# show top 250 movies
print("Top 250 movies:")
for index, top in enumerate(tops):
    if "title" in top:
        print(f"{index+1}. {top}")

# choose a random movie
print("\nRandom chosen movie:")

for index, top in enumerate(tops):
    if random_movie == index:
        print(f"{index}. {top}")
        break

print("Enjoy your watching:")
