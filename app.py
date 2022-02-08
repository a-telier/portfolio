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
    return render_template("home.html",
    projects=mongo.db.projects.find())

@app.route('/work')
def work():
    return render_template("work.html",
    projects=mongo.db.projects.find())

#   SHOW RECIPES
@app.route('/work/<project_id>')
def show_project(project_id):
    project = mongo.db.projects.find_one({"_id": ObjectId(project_id)})
    return render_template("project.html",
    projects=mongo.db.projects.find(),
    project=project)

@app.route('/about')
def about():
    return render_template("about.html")

# RUN in production by using
# flask run --host=0.0.0.0

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)