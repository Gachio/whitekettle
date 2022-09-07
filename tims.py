#!/usr/bin/env/ python
import os


from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(505)
def internal_server_error(e):
    return render_template('500.html'), 500

#manager = Manager(myapp)


if __name__ == '__main__':
    app.run(debug=True)