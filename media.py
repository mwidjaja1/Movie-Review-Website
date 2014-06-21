import webbrowser

class Movie():
	"""Creates a template for movie

	Attributes:
	title: The movie title
	storyline: The storyline
	poster_image_url: The poster image
	trailer_youtube_url: The YouTube URL	    
    """
    
    # This is a Class Variable. They apply to the entire class.
	VALID_RATINGS = ["G","PG","PG-13","R"]
    
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		"""Fetches data from a movie call

		Args:
			movie_title: The movie title
			movie_storyline: The movie storyline
			poster_image: The movie's poster
			trailer_youtube: The movie's trailer from YouTube

		Returns:
			Saves all four values as a variable under the object.
		"""
	
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
	
	def show_trailer(self):
		"""Opens up a web browser to play a given movie's trailer
		"""
		webbrowser.open(self.trailer_youtube_url)