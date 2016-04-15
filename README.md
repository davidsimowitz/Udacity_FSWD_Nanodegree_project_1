Udacity FSWD Nanodegree project 1
=================================

Udacity - Full Stack Web Developer Nanodegree
---------------------------------------------
P1: Movie Trailer Website

To build a movie trailer website where users can see your favorite movies and watch the trailers. The list of movie titles, box art, poster images, and movie trailer URLs will be stored using server side code which will then be expressed on the web page to allow users to review the movies and watch the trailers.


Requirements
------------

+ [Python](https://www.python.org/downloads/) is installed.
+ This can be verified by running the following command in the terminal:
```python
    $ python -V
```
+ [Git](https://git-scm.com/downloads) is installed.
  (Optional, if you wish to clone the project repository.)

Usage
-----

* Run the following commands to build the fresh_tomatoes.html file.
* The html page will be loaded automatically in your default browser.

```bash
$ git clone https://github.com/davidsimowitz/Udacity_FSWD_Nanodegree_project_1.git
```
  + Above command is optional.
  + Alternatively you may download the files into the directory.
```bash
$ cd Udacity_FSWD_Nanodegree_project_1
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