#!/usr/bin/env/ python
import os

from flask import Flask
from flask_script import Manager

myapp = Flask(__name__, instance_relative_config=True)

@myapp.route('/profile/<username>')
def profile(username):
    return "The Profile Section %s" % username

manager = Manager(myapp)

if __name__ == '__main__':
    #app.run(debug=True)
    manager.run()