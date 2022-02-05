import os

#   full stack framework for template development
from flask import Flask, render_template, redirect, request, url_for, session
from os import path
import datetime

#   start an instance of Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"