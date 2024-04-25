import json
from PyMovieDb import IMDB
from search import search
imdb = IMDB()
import time
from datetime import timedelta


def sort_runtime(file):
    with open(file) as f: #list of all the titles
        movieList = json.load(f)


    movieNameList = [obj['name'] for obj in movieList if 'name' in obj]


    # sort list of movie names, and track the time :
    start_time = time.perf_counter()
    for i in range(1, len(movieList)):
        key = movieList[i]
        j = i - 1
        while j >= 0 and parse_runtime_string(key['duration']) > parse_runtime_string(movieList[j]['duration']):
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







def parse_runtime_string(runtime_str):
    # Remove the 'PT' prefix
    duration_str = runtime_str[2:]
    
    # Initialize variables for hours and minutes
    hours = 0
    minutes = 0
    
    # Loop through the duration string to extract hours and minutes
    index = 0
    while index < len(duration_str):
        # Get the next digit
        num = ''
        while index < len(duration_str) and duration_str[index].isdigit():
            num += duration_str[index]
            index += 1
        
        # Get the unit (H for hours, M for minutes)
        unit = duration_str[index]
        
        # Update hours or minutes accordingly
        if unit == 'H':
            hours = int(num)
        elif unit == 'M':
            minutes = int(num)
        
        index += 1
    
    # Create a timedelta object representing the duration
    duration = timedelta(hours=hours, minutes=minutes)
    
    return duration