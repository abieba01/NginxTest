from flask import Flask
import dotenv
import os

app = Flask(__name__)
@app.route('/')
def hello_world():
        return 'Hello ' + os.environ.get('Name')