#Imports
import webbrowser

# Create the class Movie
class Movie():
    """
    This class allows users to create movie objects which contain information regarding the mevie's
    rating, title, storyline, poster, and its trailer.
    """

    # Define class variable
    movie_ratings = ["G", "PG", "PG-13", "R"]

    # Define constructor
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title #We use the value for movie_title which is passed in when we instantiate the object as self.title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def show_poster(self):
        webbrowser.open(self.poster_image_url)
