# 102

We can get python to return basic html but we don't want to write all our html code for our pages inside our [views.py](app/views.py) file as it will make it difficult to manage. Flask has the ablity to send whole files instead of just basic html.

	pip install -r requirements.txt
	python run.py
## New Files/Folders

* Create a new directory called templates inside the app directory
* Create a new file called index.html in the template directory
* Use the basic boostrap [starter template](https://getbootstrap.com/docs/4.3/getting-started/introduction/#starter-template) for the index.html file

## [requirements.txt](requirements.txt)

We need to add Jinja2 to our requirments and run 
	
	pip install -r requirements.txt

## [views.py](app/views.py)

* On the first line of our [views.py](app/views.py) file we need to add render_template to the import
* Change the index function so it returns render_template instead of just plain html
