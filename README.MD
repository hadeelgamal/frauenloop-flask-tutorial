# 105

You will notice that there is a lot of duplicate code on the index.html and restaurants.html pages. The body of the pages are slightly different but the bulk of the code is the same. This is where templates become really useful  

	python run.py

## [layout.html](app/templates/layout.html)
This is where we will define a common layout for all of the pages and just update the body of the page as we navigate through the site. Now if we need to change the design or add some features to the site it can be done in one place. We introduce the feature called blocks which is basically just a placeholder for inforamtion that we will fill in later. 

* Copy the contents of the index.html in to layout.html
* Remove everything inside the <body></body> tag and add a block placeholder called content
* Remove everything inside the <tilte></tilte> tag and add a block placeholder called


## [index.html](app/templates/index.html)
We are only concerned with the div's inside the <body></body> tags as everything else will come from our layout.html file

* remove all html that is not the a div inside the body tags
* wrap the div code in a block called content (see file)
* add the extend layout code to the top of the file
* add the block code for the title and use the heading variable for the page title


## [restaurants.html](app/templates/restaurants.html)
Repeat the same process as the index file. 