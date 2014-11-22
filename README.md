
# note2web

## To Do

* restructure directories, use nbserve name.
* working setup.py
* basic unit tests
* very simple CLI
* move to github
* CLI option to remove input cells (default true?)
* CLI option to cache / not cache
* Ability to force run from cached
* Python3 support

## Wish List


## Use Cases

* A user has run analyses in iPython Notebook and wants to easily make the
  results available on the web. The results are alreay contained
  in the notebook

* A user has analyses that need to be run regularly or on-demand, and
  the served notebooks are a way to easily generate that dynamic content.

* A user develops notebooks with extensive code, and needs a way to make
  them accessible to people who will be turned off by the code.

## Links / Inspiration

* https://github.com/joerns/ipython-notebook-tools  
* https://github.com/paulgb/runipy
* http://www.plankandwhittle.com/packaging-a-flask-web-app/

## Packaging / Deployment Strategy.

* It's a flask app. 
* It looks for notebooks (and/or a config file) in 
  the current directory.
* You install it with pip.
* You can run it three ways:

  * gunicorn note2web:uwsgi_app
  * note2web serve ... options ...
  * add it as a uswgi container to nginx, apache, etc, just like
    any other flask app.

 