import json
from PyMovieDb import IMDB
from search import search
imdb = IMDB()
import time
import random


def insertion_sort(file):
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
    
    jsonObj.append({'runtime' : abs(end_time - start_time) * 1000})


    with open('sorted.json', 'w') as json_file:
        json.dump(jsonObj, json_file,
        indent=4,
        separators=(',', ': '))
        # return the sorted json file.
        return 'sorted.json'
    


def merge_sort(file):

    with open(file) as f: #list of all the titles
        movieList = json.load(f)


    movieNameList = [obj['name'] for obj in movieList if 'name' in obj]


    def merge_sort_helper(movieNameList):
        if len(movieNameList) <= 1:
            return movieNameList

        mid = len(movieNameList) // 2
        left_half = merge_sort_helper(movieNameList[:mid])
        right_half = merge_sort_helper(movieNameList[mid:])

        return merge(left_half, right_half)

    def merge(left_half, right_half):
        merged_list = []
        left_index = right_index = 0

        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] < right_half[right_index]:
                merged_list.append(left_half[left_index])
                left_index += 1
            else:
                merged_list.append(right_half[right_index])
                right_index += 1

        merged_list.extend(left_half[left_index:])
        merged_list.extend(right_half[right_index:])
        return merged_list

    start_time = time.perf_counter()
    movieNameList = merge_sort_helper(movieNameList)
    end_time = time.perf_counter()

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

    jsonObj.append({'runtime' : abs(end_time - start_time) * 1000})


    with open('sorted.json', 'w') as json_file:
        json.dump(jsonObj, json_file,
        indent=4,
        separators=(',', ': '))
        # return the sorted json file.
        return 'sorted.json'











def quick_sort(file):

    with open(file) as f: #list of all the titles
        movieList = json.load(f)


    movieNameList = [obj['name'] for obj in movieList if 'name' in obj]

    def quick_sort_helper(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = random.choice(arr)  # Select a random pivot element
            lesser = [x for x in arr if x < pivot]
            equal = [x for x in arr if x == pivot]
            greater = [x for x in arr if x > pivot]
            return quick_sort_helper(lesser) + equal + quick_sort_helper(greater)
        
    start_time = time.perf_counter()
    movieNameList = quick_sort_helper(movieNameList)
    end_time = time.perf_counter()

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

    jsonObj.append({'runtime' : abs(end_time - start_time) * 1000})


    with open('sorted.json', 'w') as json_file:
        json.dump(jsonObj, json_file,
        indent=4,
        separators=(',', ': '))
        # return the sorted json file.
        return 'sorted.json'

    




