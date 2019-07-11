#Imports
import webbrowser

# Create the class Movie
class Movie():
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
