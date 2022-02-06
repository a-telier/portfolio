import os
from os import path

from flask import Flask, render_template, redirect, request, url_for, session
import datetime

#   start an instance of Flask
app = Flask(__name__)

#   import env as config, also works
if path.exists("env.py"):
    import env

@app.route("/")
@app.route('/home')
def index():
    return render_template("index.html")

# RUN in production by using
# flask run --host=0.0.0.0

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)