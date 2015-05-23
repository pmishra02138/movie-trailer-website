class Movie(object):
    """Movie class with title, poster url and youtube trailer url """
    def __init__(self, title, posterUrl, trailerUrl):
        self.title = title
        self.poster_image_url = posterUrl
        self.trailer_youtube_url = trailerUrl
