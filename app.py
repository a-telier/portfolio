import os
from flask import Flask, render_template, redirect, request, url_for, session

from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

from os import path
import bcrypt

import datetime

#############################################
#    CONFIGURATION
#############################################

app = Flask(__name__)

#   import env as config
if path.exists("env.py"):
    import env

#   configuration of database
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


#############################################
#    PAGES
#############################################

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