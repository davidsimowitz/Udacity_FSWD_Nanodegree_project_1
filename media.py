class Movie():
    """
    Movie information
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """
        Initialize variables
        :param title: movie name
        :param poster_image_url: link to movie poster image
        :param trailer_youtube_url: link to movie trailer (YouTube)
        :return: None
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url