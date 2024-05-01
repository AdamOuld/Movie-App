from lxml_html_clean import clean_html
from flask import Flask, render_template
from flask import Flask, render_template, request, jsonify
import json
from sort import insertion_sort, merge_sort, quick_sort
from sort_rating import sort_rating_i, sort_rating_m, sort_rating_q
from sort_date import sort_date_i, sort_date_m, sort_date_q
from sort_runtime import sort_runtime_i, sort_runtime_m, sort_runtime_q


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')






@app.route('/api/data/name/insertionsort', methods=['GET'])
def get_data_i():
    input = insertion_sort('static/data.json')
    with open(input, 'r') as file:
        json_data = json.load(file)
    data = {'message': json_data}
    return (data), "7"

@app.route('/api/data/name/mergesort', methods=['GET'])
def get_data_m():
    input = merge_sort('static/data.json')
    with open(input, 'r') as file:
        json_data = json.load(file)
    data = {'message': json_data}
    return (data), "7"

@app.route('/api/data/name/quicksort', methods=['GET'])
def get_data_q():
    input = quick_sort('static/data.json')
    with open(input, 'r') as file:
        json_data = json.load(file)
    data = {'message': json_data}
    return (data), "7"










@app.route('/api/data/rating/insertionsort', methods=['GET'])
def get_data_rating_i():
    input = sort_rating_i('static/data.json')
    with open(input, 'r') as file:
        json_data = json.load(file)
    data = {'message': json_data}
    return (data), "7"


@app.route('/api/data/rating/mergesort', methods=['GET'])
def get_data_rating_m():
    input = sort_rating_m('static/data.json')
    with open(input, 'r') as file:
        json_data = json.load(file)
    data = {'message': json_data}
    return (data), "7"


@app.route('/api/data/rating/quicksort', methods=['GET'])
def get_data_rating_q():
    input = sort_rating_q('static/data.json')
    with open(input, 'r') as file:
        json_data = json.load(file)
    data = {'message': json_data}
    return (data), "7"




@app.route('/api/data/date/insertionsort', methods=['GET'])
def get_data_date_i():
    input = sort_date_i('static/data.json')
    with open(input, 'r') as file:
        json_data = json.load(file)
    data = {'message': json_data}
    return (data), "7"

@app.route('/api/data/date/mergesort', methods=['GET'])
def get_data_date_m():
    input = sort_date_m('static/data.json')
    with open(input, 'r') as file:
        json_data = json.load(file)
    data = {'message': json_data}
    return (data), "7"

@app.route('/api/data/date/quicksort', methods=['GET'])
def get_data_date_q():
    input = sort_date_q('static/data.json')
    with open(input, 'r') as file:
        json_data = json.load(file)
    data = {'message': json_data}
    return (data), "7"





@app.route('/api/data/runtime/insertionsort', methods=['GET'])
def get_data_runtime_i():
    input = sort_runtime_i('static/data.json')
    with open(input, 'r') as file:
        json_data = json.load(file)
    data = {'message': json_data}
    return (data), "7"


@app.route('/api/data/runtime/mergesort', methods=['GET'])
def get_data_runtime_m():
    input = sort_runtime_m('static/data.json')
    with open(input, 'r') as file:
        json_data = json.load(file)
    data = {'message': json_data}
    return (data), "7"


@app.route('/api/data/runtime/quicksort', methods=['GET'])
def get_data_runtime_q():
    input = sort_runtime_q('static/data.json')
    with open(input, 'r') as file:
        json_data = json.load(file)
    data = {'message': json_data}
    return (data), "7"






if __name__ == '__main__':
    app.run(debug=True, port=8000)