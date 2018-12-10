Movie Trailer Website
=================================


Udacity - Full Stack Web Developer Nanodegree
---------------------------------------------
P1: Movie Trailer Website

This project's objective was to design and build the server-side code necessary to dynamically generate a movie trailer website—where users can view your favorite movies and watch their trailers—from a Python data structure. The list of movies—each including a title, poster, and trailer—is parsed from a text file allowing the static web page to be updated easily after editing the movie list.


Requirements
------------

+ [Python](https://www.python.org/downloads/) is installed.
+ This can be verified by running the following command in the terminal:
```bash
$ python -V
```
+ [Git](https://git-scm.com/downloads) is installed.
  (Optional, if you wish to clone the project repository.)


Usage
-----

* Run the following commands to build the fresh_tomatoes.html file.
* The html page will be loaded automatically in your default browser.

```bash
$ git clone https://github.com/davidsimowitz/fullstack-nanodegree-project-1.git
```
  + Above command is optional.
  + Alternatively you may download the files into the directory.
```bash
$ cd fullstack-nanodegree-project-1
```
  + Verify the following files are present before continuing:
    * media.py
    * fresh_tomatoes.py
    * entertainment_center.py
    * movie_details.txt

```bash
$ python entertainment_center.py
```
  + fresh_tomatoes.html will load in your default browser once the above command is ran.


Customized Movies (optional)
----------------------------

Input is accepted from a file named movie_details.txt that resides in the project directory. This file can be modified to display the movies of your choosing. The format for movie_details.txt is as follows:

1. The first line must contain the number of movies.
2. Then for each movie, you must enter three pieces of information, each on their own line:
    * first its title
    * followed next by a url to its movie poster image
    * followed lastly by a link to its trailer on YouTube
3. A movie_details.txt file has been included.
