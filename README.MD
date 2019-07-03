# 103

Static text is useful but sometime we will need to dynamically allocate the information. This is where variables are useful. 

	python run.py


## [views.py](app/views.py)
In out index function we create
* Two string variables
* A list of foods. Lists in python are the same as array's in javascript
* Update the render_template function to include the variables created. 

## [index.html](app/templates/index.html)

* Change our basic H1 to a jumbotron and render some variables
* Create an unordered list of foods