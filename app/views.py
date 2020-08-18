from flask import Flask, render_template, url_for, request
from app import app
from pexels_api import API

import requests, json

PEXELS_API_KEY = '563492ad6f917000010000010ba04980d06044c3aa4329eb1e8baf97'


@app.route('/')
def index():
    heading = "Photography Agency"
    subheading = "Our work"
    # Import API class from pexels_api package
    # Type your Pexels API
    # Create API object
    fashion_api = API(PEXELS_API_KEY)
    building_api = API(PEXELS_API_KEY)
    # Search five 'kitten' photos
    fashion_api.search('fashion', page=1, results_per_page=20)
    building_api.search('building', page=1, results_per_page=20)


    # Get photo entries
    fashion = fashion_api.get_entries()
    building = building_api.get_entries()


    return render_template('index.html',heading=heading, subheading=subheading, fashion=fashion, building=building)

# @app.route('/')
# def index():
# 	heading = "Python Tutorial"
# 	subheading = "This is the subheading of our page"
# 	foods = ['pasta','pizza','salad','dessert']
# 	return render_template('index.html', heading=heading, subheading=subheading, foods=foods)

# @app.route('/restaurants')
# def get_restaurants():
# 	heading = "restaurants"
# 	subheading = "A selection of the best places to eat locally"
# 	return render_template('restaurants.html', heading=heading, subheading=subheading, restaurants=restaurants)

@app.route('/OurTeam')
def OurTeam():
    heading = "Our Team"
    subheading = "Our Team"
    url = "https://randomuser.me/api/?results=10"
    response = requests.get(url, verify=False)
    # return "<html><body><h1>ttttt</h1></body></html>"
    return render_template('ourteam.html', heading=heading, subheading=subheading, people=response.json())


@app.route('/project/<proj_id>')
def projectDetail(proj_id):
    header = {"Authorization": PEXELS_API_KEY}
    url = "https://api.pexels.com/v1/photos/" + str(proj_id)
    response = requests.get(url=url, headers=header)
    return render_template('detail.html', project=response.json())
