'''
File Name: cybercipher.py
Create: 12/15/2024
Description: The launch file of Flask
'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello worldddddddd!"

if __name__ == '__main__':
    app.run(debug = True)