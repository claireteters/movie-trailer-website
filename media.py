import webbrowser
class Movie():
    """This provides a way to store movie related info
    Attributes:
        title: A string to store the title of the movie.
        storyline: A string to store the basic plot of the movie.
        poster_image_url: A string to store the URL of the movie poster.
        trailer_youtube_url: A string to store the URL of the movie trailer.
        release_year: A string to store the release year of the movie.
        rating: A string to store the rating of the movie.
    """

    """Initialises Movie class instance variables."""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_release_year, movie_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_year = movie_release_year
        self.rating = movie_rating

    """Plays the movie trailer in the web browser."""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    