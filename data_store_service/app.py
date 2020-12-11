from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from configparser import ConfigParser
from flask_pymongo import PyMongo
from bson.json_util import dumps # Takes the bson data from the database and convert to json
import json
import os



app = Flask(__name__)



    
password = 'yLYfckRV0zleZm7Z'
username = 'prezlo'
mongo_uri = 'cougar-data-den-otljj.mongodb.net/campusDB?retryWrites=true&w=majority'
db_name = 'campusDB'



app.config['MONGO_DBNAME'] = db_name
app.config['MONGO_URI'] = f'mongodb+srv://{username}:{password}@{mongo_uri}'
mongo = PyMongo(app)




@app.route('/')
def home():
    
    return "Living Campus API v2 "

# This route allows iOS applications to post its form content to MongoDB Atlas
@app.route('/api/v2/submit', methods=['POST'])
def send_to_db():
    request_data = request.get_json()

    person_name = 'not-available'
    res = not bool(request_data)
    if res:
        packet = {
            # 10/22/2019 - Updated 
            'temp-rating' : request_data['temp-rating'],
            'name': request_data['name']
            }
    cougar_profiles = mongo.db['cougar_profiles']
    cougar_profiles.insert_one(packet)
    return jsonify({'message':'success.'}), 200

@app.route('/api/v2/ingest', methods=['POST'])
def ingest_data():
    request_data = request.get_json()
    hasData = not bool(request_data)
    if hasData:
        packet = {
            'temp-rating' : request_data['topic'],
            'name' : request_data['data']
        }
    cougar_profiles = mongo.db['cougar_profiles']
    cougar_profiles.insert_one(packet)
    return jsonify({'message':'success.'}), 200


    
# when a user hits this endpoint the server will respond with available data in the mongoDB database

@app.route('/api/v1/fetch')
def queryDB():
    cougar_profiles = mongo.db['cougar_profiles']
    results = cougar_profiles.find({})
    return jsonify({"success": json.loads(dumps(results))})



if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
