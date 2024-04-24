import json
from PyMovieDb import IMDB
from search import search
imdb = IMDB()
import time


def sort(file):
    with open(file) as f: #list of all the titles
        movieList = json.load(f)


    movieNameList = [obj['name'] for obj in movieList if 'name' in obj]


    # sort list of movie names, and track the time :
    start_time = time.perf_counter()
    for i in range(1, len(movieNameList)):
        key = movieNameList[i]
        j = i - 1
        while j >= 0 and key < movieNameList[j]:
            movieNameList[j + 1] = movieNameList[j]
            j -= 1
            movieNameList[j + 1] = key
    end_time = time.perf_counter()
    print("The sorting algorithm took", abs(start_time - end_time), "seconds to run")
    # use the search function from search.py that takes the name of the movie as the input
    # and goes through the data.json file to return the json object of the corresponding movie
    jsonObj = []
    for movie in movieNameList:
        data = search('static/data.json', movie)
        if not (data.get('review') is None):
            del data['review']
        if not (data.get('description') is None):
            del data['description']
        if not (data.get('actor') is None):
            del data['actor']
        if not (data.get('creator') is None):
            del data['creator']
        if not (data.get('keywords') is None):
            del data['keywords']
        if not (data.get('director') is None):
            del data['director']




        jsonObj.append(data)


    with open('sorted.json', 'w') as json_file:
        json.dump(jsonObj, json_file,
        indent=4,
        separators=(',', ': '))
        # return the sorted json file.
        return 'sorted.json'