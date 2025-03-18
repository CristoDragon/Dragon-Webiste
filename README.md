# Dragon-Webiste
This repository contains code to build a personal website to show project experience.

# Git Workflow
1. Develop features in dev branch
2. Once stable, merge into main branch
3. Pull and deploy on server

# WSGI file
1. What is it: WSGI (Web Server Gateway Interface) file is a configuration file that connects your Flask application to the PythonAnywhere web server (which uses Gunicorn behind the scenes). It's like the bridge between your Python code and the web server. Instead of running python app.py manually, PythonAnywhere uses the WSGI file to load your Flask app automatically whenever someone visits your website.

2. How does it work:
    (1) The web server receives a request (e.g., someone visits https://bigdragon45.pythonanywhere.com/).
    (2) The WSGI file tells the server how to find and run your Flask app.
    (3) Your Flask app processes the request and returns a response.
    (4) The server sends the response back to the user.
