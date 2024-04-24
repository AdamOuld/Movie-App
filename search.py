import json




def search(file, movieName):


with open(file) as f:
movieList = json.load(f)


movieNameList = [obj['name'] for obj in movieList if 'name' in obj]


# we have the movie name, and the movie name list
# we just need to search for it


for i in range(len(movieNameList)):
if movieNameList[i] == movieName:
return movieList[i]


# Movie not found in the list
return movieList[0]