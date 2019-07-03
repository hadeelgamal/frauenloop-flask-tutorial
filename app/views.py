from flask import Flask, render_template
from app import app

@app.route('/')
def index():
	heading = "Python Tutorial"
	subheading = "This is the subheading of our page"
	foods = ['pasta','pizza','salad','dessert']
	return render_template('index.html', heading=heading, subheading=subheading, foods=foods)
