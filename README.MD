# 106

So far we have just been using the standard bootstrap framework. We will want to add some custom css to our project. For this we need to create a new folder called static inside our app folder on the same level as templates. As we will probably need to add images, js and css our project I suggest creating a folder for each of these types so the project is a bit more organized. 

Images and JS can be added a similar way

	python run.py


## [custom.css](app/static/css/custom.css)
Add any custom css that you need to this file. I am just changing the background color for now as a sample 

## [views.py](app/views.py)
We need to add url_for to our import on the first line. url_for generates the url the asset based on the server setup. 

## [layout.html](app/templates/layout.html)
As we want to include the css on all the pages of our site we add the following code to the just before the closing </head> tag. 

	<link rel="stylesheet" href="{{ url_for('static', filename='css/custom.css') }}">