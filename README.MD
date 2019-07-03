# 104

Now that we have some basic variables in place lets create a new page that lists out restaurants that we have in a dictionary (A python dictionary is similar to a JSON object) 

	python run.py


## [views.py](app/views.py)
* Create a new route and new function for our restuaruants page. 
* Inside the function render the template for restaurants and pass it the heading, subheading and dictionary of restaurants. 

## [restaurants.html](app/templates/restaurants.html)

* Create a new html file. You can copy the index.html and modify it slightly
* Display a list of restaurant names and their address. 