# 107

DRY (Don't Repeat Yourself) is coding principal which aims to reduce repeating code. If we look at the two pages that we have created so far both contain a jumbotron with the same code. A jumbotron is a part of a page that can be referred to as a partial. Lets create a folder for these partials in our template directory. 

	python run.py


## [jumbotron.html](app/templates/partials/jumbotron.html)
In our partials folder we create a jumbotron.html file and add the jumbotron code to the page. This can be taken directly from the [index.html](app/templates/index.html) or [restaurants.html](app/templates/restaurants.html)

## [index.html](app/templates/index.html) and [restaurants.html](app/templates/restaurants.html)
We remove the existing jumbotron code and use an include. 

	{% include 'partials/jumbotron.html' %}

Your navigation and footer are also a good elements that can be added as partials. 