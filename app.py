from lxml_html_clean import clean_html
from flask import Flask, render_template
from flask import Flask, render_template, request, jsonify
import json
from sort import sort


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')






@app.route('/api/data', methods=['GET'])
def get_data():
    input = sort('static/data.json')
    with open(input, 'r') as file:
        json_data = json.load(file)
    data = {'message': json_data}
    return (data), "7"






if __name__ == '__main__':
    app.run(debug=True, port=8000)