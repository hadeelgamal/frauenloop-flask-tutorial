from flask import Flask
from app import app

@app.route('/')
def index():
	return "<h1>Hello World!</h1>"
