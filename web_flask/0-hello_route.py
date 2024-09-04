#!/usr/bin/python3
"""
Start Flask application
"""

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """Returns Hello HBNB!"""
    return 'Hello HBNB!'

@app.route('/airbnb-onepage/', strict_slashes=False)
def airbnb_onepage():
    """Returns a message for the /airbnb-onepage/ route"""
    return 'Welcome to Airbnb Onepage!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
