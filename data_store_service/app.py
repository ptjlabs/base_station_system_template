from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from configparser import ConfigParser
from flask_pymongo import PyMongo
from bson.json_util import dumps # Takes the bson data from the database and convert to json
import json
import os



app = Flask(__name__)
parser = ConfigParser()
password = ""
username = ""
mongo_uri = ""
db_name = ""

#configPath = r'C:\Users\preston.turner\Desktop\base_station\data_store_service\dev.ini'
configPath = r'.\data_store_service\dev.ini'
parser.read(configPath)
    
password = parser.get('MONGO','password')
username = parser.get('MONGO','username')
mongo_uri = parser.get('MONGO','mongouri')
db_name = parser.get('MONGO','dbname')



app.config['MONGO_DBNAME'] = db_name
app.config['MONGO_URI'] = f'mongodb+srv://{username}:{password}@{mongo_uri}'
mongo = PyMongo(app)




@app.route('/')
def home():
    
    return "Living Campus API v2 "

# This route allows iOS applications to post its form content to MongoDB Atlas
@app.route('/api/v1/submit', methods=['POST'])
def send_to_db():
    request_data = request.get_json()

    person_name = 'not-available'
    if request_data['name'] != None or request_data['name'] != "":
        person_name = request_data['name']
    packet = {
        # 10/22/2019 - Updated 
        'temp-rating' : request_data['temp-rating'],
        'name': person_name
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
