import json
from PyMovieDb import IMDB
from search import search
imdb = IMDB()
import time

from datetime import datetime


def sort_date(file):
    with open(file) as f: #list of all the titles
        movieList = json.load(f)


    movieNameList = [obj['name'] for obj in movieList if 'name' in obj]


    # sort list of movie names, and track the time :
    start_time = time.perf_counter()
    for i in range(1, len(movieList)):
        key = movieList[i]
        j = i - 1
        while j >= 0 and datetime.strptime(key['datePublished'], '%Y-%m-%d') < datetime.strptime(movieList[j]['datePublished'], '%Y-%m-%d'):
            movieList[j + 1] = movieList[j]
            j -= 1
            movieList[j + 1] = key
    end_time = time.perf_counter()
    print("The sorting algorithm took", abs(start_time - end_time), "seconds to run")
    # use the search function from search.py that takes the name of the movie as the input
    # and goes through the data.json file to return the json object of the corresponding movie
    jsonObj = []
    for movie in movieList:
        jsonObj.append(movie)


    with open('sorted.json', 'w') as json_file:
        json.dump(jsonObj, json_file,
        indent=4,
        separators=(',', ': '))
        # return the sorted json file.
        return 'sorted.json'