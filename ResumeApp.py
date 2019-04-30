from flask import Flask, render_template,request,redirect,url_for # For flask implementation
from pymongo import MongoClient # Database connector
from bson.objectid import ObjectId # For ObjectId to work
from bson.errors import InvalidId # For catching InvalidId exception for ObjectId
import pprint
import json
from flask import jsonify 


client = MongoClient('localhost', 27017) #Configure the connection to the database
db = client.resumeDB #Select the database

app = Flask(__name__)
app._static_folder = '/home/me/ResumeApp/static'
title = "Resume with Flask and MongoDB"
heading = "Edgar Aguiniga - Software Engineer"

@app.route('/')
def index():
    resume = get_resume()
    return render_template('resume.html', resume=resume)

@app.route('/preview', methods=['POST'])
def preview():
    resume = request.json
    #return 'preview ' + str(type(resume)) + ' <-- val' 
    return render_template('resume_c.html', resume=resume)

@app.route('/edit')
def edit():
    resume = get_resume()
    return render_template('resume_js.html', resume=resume)

@app.route('/get')
def show_resume():
    #return get_resume()
    with open('resume.json') as infile:
        resume = json.loads(infile.read())
        return jsonify(resume)

@app.route('/rm')
def rm_resume():
    db.resumeDB.deleteMany()
    return 'resume removed'

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

@app.route('/save', methods=['POST'])
def add_resume():
    resume = request.json
    db.resumeDB.insert_one(resume)
    return 'resume inserted'
    
def get_resume():
    return db.resumeDB.find_one()
