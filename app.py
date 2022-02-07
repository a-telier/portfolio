import os
from os import path

from flask import Flask, render_template, redirect, request, url_for, session

#   Mongo DB manipulation libraries
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

#   used in datepicker
import datetime

#   start an instance of Flask
app = Flask(__name__)

#   import env as config
if path.exists("env.py"):
    import env

#   configuration of Database
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['MONGODB_NAME'] = os.environ.get('MONGODB_NAME')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

#   create an instance of PyMongo
mongo = PyMongo(app)

@app.route("/")
@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/work')
def work():
    return render_template("work.html",
    projects=mongo.db.projects.find())

# RUN in production by using
# flask run --host=0.0.0.0

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)