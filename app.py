import os

#   full stack framework for template development
from flask import Flask, render_template, redirect, request, url_for, session
from os import path
import datetime

#   start an instance of Flask
app = Flask(__name__)

@app.route("/")
@app.route('/home')
def index():
    return render_template("index.html")

# RUN in production by using run --host=0.0.0.0