# This imports the media.py file
import media
import fresh_tomatoes

# This creates an object Toy Story from the class 'Movie' in media.py
toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

# This creates an object Monsters Inc  from the class 'Movie' in media.py
monsters = media.Movie("Monsters Inc.",
				 "Two monsters go on a journey trying to scare children for power",
				 "http://upload.wikimedia.org/wikipedia/en/6/63/Monsters_Inc.JPG",
				 "https://www.youtube.com/watch?v=8IBNZ6O2kMk")

# This creates an object Finding Nemo from the class 'Movie' in media.py
nemo = media.Movie("Finding Nemo",
				 "An clownfish swims over the world to try and find his son",
				 "http://www.redesignrevolution.com/wp-content/uploads/2012/09/Finding-Nemo-Alternative-Movie-Posters-7.jpg",
				 "https://www.youtube.com/watch?v=wZdpNglLbt8")

# This creates an object Ratatouille from the class 'Movie' in media.py
rat = media.Movie("Ratatouille",
				 "A rat tries to achieve his dream, that anyone can cook",
				 "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
				 "https://www.youtube.com/watch?v=c3sBBRxDAqk")

# This creates an object Up from the class 'Movie' in media.py
up = media.Movie("Up",
				 "An elderly man goes on an adventure with a boy, a bird, & a dog",
				 "http://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
				 "https://www.youtube.com/watch?v=xxMcViTf7KU")

# This creates an object Brave from the class 'Movie' in media.py
brave = media.Movie("Brave",
				 "A princess breaks the mold and tries to be herself",
				 "http://upload.wikimedia.org/wikipedia/en/9/96/Brave_Poster.jpg",
				 "https://www.youtube.com/watch?v=TEHWDA_6e3M")
				 
# Creates an Array with our movies
movies = [toy_story, monsters, nemo, rat, up, brave]

# Print Info on Toy Story's Title
# print(toy_story.title)

# Prints all Valid Ratings
# print(media.Movie.VALID_RATINGS)

# Opens a Movie Page using the fresh_tomatoes.py file
# fresh_tomatoes.open_movies_page(movies)