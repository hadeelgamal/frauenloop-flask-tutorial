# 108

Pulling data from an API in python is quite easy in comparison to Javascript. As we have already used the random user API in a previous project lets use it again here.   

	python run.py

## [requirements.txt](requirements.txt)
Here we add the requests library to our file. We also need to do a pip install of the new requirements. 

	pip install -r requirements.txt

## [views.py](app/views.py)
Add request to the import so we can use it. 

	from flask import Flask, render_template, url_for, request

We also need to import the reuests and json library
	
	import requests, json

Now we need to create a new route and function for the page that pulls in randon users. The response the comes back we pass to the template in json format. 
	
	@app.route('/randomusers')
	def randos():
    	heading = "API's"
    	subheading = "Accessing the Random User API"
    	url = "https://randomuser.me/api/?results=50"
    	response = requests.request("GET", url)
    	return render_template('randomusers.html', heading=heading, subheading=subheading, people=response.json())

## [randomusers.html](app/templates/randomusers.html)
This will be very similar to the exiting restaurants.html file so we can duplicate that to start. Change the for loop slightly to itterate over the data we get back from the server and extract the inforamtion we need to list all the names. Once you get the basic information you should improve the design on the page. 
