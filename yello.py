#!/usr/bin/env/ python

from flask import Flask
from flask_script import Manager

app = Flask(__name__)

@app.route('/profile/<username>')
def profile(username):
    return "The Profile Section %s" % username

manager = Manager(app)

if __name__ == '__main__':
    #app.run(debug=True)
    manager.run()