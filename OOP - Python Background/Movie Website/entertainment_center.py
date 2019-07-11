#Imports
import media
import fresh_tomatoes

# instantiate a new movie object called toy story
toy_story = media.Movie('Toy Story 4',
                        'A room full of toys which come to life!',
                        'en.wikipedia.org/wiki/Toy_Story_4#/media/File:Toy_Story_4_poster.jpg',
                        'https://www.youtube.com/watch?v=wmiIUN-7qhE')
#print(toy_story.title)

#Instantiate a new movie object called Avatar
avatar = media.Movie('Avatar',
                     'A marine on an alien planet!',
                     'https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg',
                     'https://www.youtube.com/watch?v=6ziBFh3V1aM')

#print(avatar.storyline)
#avatar.show_trailer()

# instantiate a new movie object called Inception
inception = media.Movie('Inception',
                        'A film in which dreams become a reality - or maybe the other way around...',
                        'https://assets.www.warnerbros.com/sites/default/files/inception_posterlarge_8-1308772917.jpg',
                        'https://www.youtube.com/watch?v=YoHD9XEInc0')

#inception.show_poster()

movies = [toy_story, avatar, inception]
fresh_tomatoes.open_movies_page(movies)
