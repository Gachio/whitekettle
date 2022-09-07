#!/usr/bin/env/ python
#from ensurepip import bootstrap

#import os

from flask_bootstrap import Bootstrap
from flask import Flask 
from flask import render_template
from flask_moment import Moment
from datetime import datetime
#from flask_script import Manager

moment = Moment(app)
app = Flask(__name__, instance_relative_config=True)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

#manager = Manager(myapp)

if __name__ == '__main__':
    app.run(debug=True)
    #manager.run()