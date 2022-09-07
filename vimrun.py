#!/usr/bin/env/ python

from flask import Flask
app = Flask(__name__)


@app.route('/')

def search4vowels(word):
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

search4vowels("hitch hiker")

if __name__ == '__main__':
    app.run(debug=True)