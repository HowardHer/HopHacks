"""
from pythonprac import squared
print(squared(10))
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello World"