# Author: Dragon Xu
# Date: 3/16/2025
# Description: This is a Flask application that serves a web page to show personal profiles and experiences.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
