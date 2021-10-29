# Import Modules
from flask import Flask, jsonify, request
from data import data 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route('/')
def index():
    return(jsonify({
        "data" : data,
        "message" : "success"
    }),200)

@app.route('/star')
def star():
    name = request.args.get('name')
    star_data = next(item for item in data if item["name"] == name)
    return(jsonify({
        "data" : star_data,
        "message" : "success"
    }),200)

if (__name__ == '__main__'):
    app.run(debug=True)