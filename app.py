from lxml_html_clean import clean_html
from flask import Flask, render_template
from flask import Flask, render_template, request, jsonify
import json
from sort import sort
from sort_rating import sort_rating
from sort_date import sort_date


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')






@app.route('/api/data/name', methods=['GET'])
def get_data():
    input = sort('static/data.json')
    with open(input, 'r') as file:
        json_data = json.load(file)
    data = {'message': json_data}
    return (data), "7"


@app.route('/api/data/rating', methods=['GET'])
def get_data_rating():
    input = sort_rating('static/data.json')
    with open(input, 'r') as file:
        json_data = json.load(file)
    data = {'message': json_data}
    return (data), "7"


@app.route('/api/data/date', methods=['GET'])
def get_data_date():
    input = sort_date('static/data.json')
    with open(input, 'r') as file:
        json_data = json.load(file)
    data = {'message': json_data}
    return (data), "7"






if __name__ == '__main__':
    app.run(debug=True, port=8000)