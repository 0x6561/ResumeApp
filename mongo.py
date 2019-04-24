from flask import Flask, render_template,request,redirect,url_for # For flask implementation
from pymongo import MongoClient # Database connector
from bson.objectid import ObjectId # For ObjectId to work
from bson.errors import InvalidId # For catching InvalidId exception for ObjectId
import pprint
import json
from flask import jsonify 


client = MongoClient('localhost', 27017) #Configure the connection to the database
db = client.databaseDB #Select the database

app = Flask(__name__)
title = "Resume with Flask and MongoDB"
heading = "Edgar Aguiniga - Software Engineer"

@app.route('/')
def show_resume():
    #return get_resume()
    with open('resume.json') as infile:
        resume = json.loads(infile.read())
        return jsonify(resume)
        #return str(resume)
        #return app.response_class(resume, content_type='application/json')

# save resume to file (json)
# requires a dict as a parameter
def save_resume(resume):
    with open('resume.json', 'w') as outfile:
        json.dump(resume, outfile, indent=4, sort_keys=False, default=str)

# read resume from file (json)
# returns a dict
def read_resume():
    with open('resume.json') as infile:
        resume = json.loads(infile.read())
        return resume


def add_resume(resume):
    db.resumeDB.insert_one(resume)
    
def get_resume():
    return db.resumeDB.find_one()
