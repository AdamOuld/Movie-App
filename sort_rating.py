import json
from PyMovieDb import IMDB
from search import search
imdb = IMDB()
import time
import random


def sort_rating_i(file):
    with open(file) as f: #list of all the titles
        movieList = json.load(f)


    movieNameList = [obj['name'] for obj in movieList if 'name' in obj]


    # sort list of movie names, and track the time :
    start_time = time.perf_counter()
    for i in range(1, len(movieList)):
        key = movieList[i]
        j = i - 1
        while j >= 0 and key['rating']['ratingValue'] > movieList[j]['rating']['ratingValue']:
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
    
    jsonObj.append({'runtime' : abs(end_time - start_time) * 1000})


    with open('sorted.json', 'w') as json_file:
        json.dump(jsonObj, json_file,
        indent=4,
        separators=(',', ': '))
        # return the sorted json file.
        return 'sorted.json'
    

def sort_rating_m(file):

    with open(file) as f: #list of all the titles
        movieList = json.load(f)


    movieNameList = [obj['name'] for obj in movieList if 'name' in obj]


    def merge_sort_helper(movieList):
        if len(movieList) <= 1:
            return movieList

        mid = len(movieList) // 2
        left_half = merge_sort_helper(movieList[:mid])
        right_half = merge_sort_helper(movieList[mid:])

        return merge(left_half, right_half)

    def merge(left_half, right_half):
        merged_list = []
        left_index = right_index = 0

        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index]['rating']['ratingValue'] > right_half[right_index]['rating']['ratingValue']:
                merged_list.append(left_half[left_index])
                left_index += 1
            else:
                merged_list.append(right_half[right_index])
                right_index += 1

        merged_list.extend(left_half[left_index:])
        merged_list.extend(right_half[right_index:])
        return merged_list

    start_time = time.perf_counter()
    movieList = merge_sort_helper(movieList)
    end_time = time.perf_counter()

    jsonObj = []
    for movie in movieList:
        jsonObj.append(movie)

    jsonObj.append({'runtime' : abs(end_time - start_time) * 1000})


    with open('sorted.json', 'w') as json_file:
        json.dump(jsonObj, json_file,
        indent=4,
        separators=(',', ': '))
        # return the sorted json file.
        return 'sorted.json'
    

def sort_rating_q(file):

    with open(file) as f: #list of all the titles
        movieList = json.load(f)


    movieNameList = [obj['name'] for obj in movieList if 'name' in obj]

    def quick_sort_helper(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = random.choice(arr)['rating']['ratingValue']  # Select a random pivot element
            lesser = [x for x in arr if x['rating']['ratingValue'] > pivot]
            equal = [x for x in arr if x['rating']['ratingValue'] == pivot]
            greater = [x for x in arr if x['rating']['ratingValue'] < pivot]
            return quick_sort_helper(lesser) + equal + quick_sort_helper(greater)
        
    start_time = time.perf_counter()
    movieList = quick_sort_helper(movieList)
    end_time = time.perf_counter()

    

    jsonObj = []
    for movie in movieList:
        jsonObj.append(movie)

    jsonObj.append({'runtime' : abs(end_time - start_time) * 1000})

    with open('sorted.json', 'w') as json_file:
        json.dump(jsonObj, json_file,
        indent=4,
        separators=(',', ': '))
        # return the sorted json file.
        return 'sorted.json'