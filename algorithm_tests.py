import json

from os import path

import time

from PyMovieDb import IMDB

imdb = IMDB()


data_filename = "static/data.json"

if path.isfile(data_filename) is False:
    raise Exception("File not found")



def track_time(sort, arr):
    start_time = time.perf_counter()
    sort(arr)
    end_time = time.perf_counter()
    print("The sorting algorithm took", abs(start_time - end_time), "seconds to run")
    return start_time - end_time


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Merge the two halves into a single sorted array
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left and right arrays
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)  # Select a random pivot element
        lesser = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quick_sort(lesser) + equal + quick_sort(greater)



total_seconds = 0
for i in range(0, 10000):
    with open(data_filename) as f:
        movieList = json.load(f)

    movieNameList = [obj['name'] for obj in movieList if 'name' in obj]
    total_seconds += abs(track_time(insertion_sort, movieNameList))

average_seconds = total_seconds / 10000
print(average_seconds)