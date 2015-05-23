from media import Movie
from fresh_tomatoes import open_movies_page

inception = Movie('Inception', 'http://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg',
                    'https://www.youtube.com/watch?v=66TuSJo4dZM')

the_homesman = Movie('The Homesman', 'http://upload.wikimedia.org/wikipedia/en/f/f5/The_Homesman_poster.jpg',
                    'https://www.youtube.com/watch?v=kiWXNfsrN4Q')

avatar = Movie('Avatar', 'http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
                    'https://www.youtube.com/watch?v=_Tkc5pQp_JE')


movies = [inception, the_homesman, avatar]

open_movies_page(movies)
