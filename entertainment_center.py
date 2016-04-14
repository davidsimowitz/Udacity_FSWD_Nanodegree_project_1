import media
from fresh_tomatoes import *

def movie_reader(filename):
    """
    parse movie information file and extract
    information to build a list of movie objects.
    :param filename: input file containing movie information
    :return movies: initialize a list of movie objects.
    """
    with open(filename) as file_object:
        lines = file_object.readlines()
    number_of_movies = int(lines[0].strip())
    movie_details = 3
    movies = []
    for movie_number in range(1, number_of_movies + 1):
        index = movie_number * movie_details - (movie_details - 1)
        title = lines[index].strip().title()
        poster = lines[index + 1].strip()
        trailer = lines[index + 2].strip()
        movie = media.Movie(title, poster, trailer)
        movies.append(movie)
    return movies

filename = 'movie_details.txt'
movies = movie_reader(filename)
open_movies_page(movies)