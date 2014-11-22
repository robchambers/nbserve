# nbserve

`nbserve` is a simple script that lets you serve
iPython notebooks as read-only HTML files over the web.

One of the key differences between nbserve and other options
(like nbviewer) is that it lets you *run* the files as
they're being served, allowing you to create dynamic,
always-up-to-date 'reports'.

As nbserve matures, I hope to add features like:

* Stripping of input cells.
* Caching, with some simple defaults and features to minimize
  the amount of configuration required.
* Convenient/appropriate output templates.
* Password protection
* An example of how to deploy to Heroku or similar.

## Usage

1) Checkout the Git repo.
2) Set up:

   ```sh
   $ python setup.py develop
   # or
   $ python setup.py install
   ```

3) Run it:

   ```
   $ nbserve -h

       usage: nbserve [-h] [-v] [-p PORT] [--no-debug] [working_directory]

       nbserve is a simple script that lets you serve iPython notebooks as read-only
       HTML files over the web. It has some default options that make the notebooks
       appropriate for generating reports, such as hiding input cells.

       positional arguments:
         working_directory

       optional arguments:
         -h, --help         show this help message and exit
         -v, --version      show program's version number and exit
         -p PORT
         --no-debug

   $ nbserve

       Ctrl-C to stop server.
        * Running on http://127.0.0.1:5000/
        * Restarting with reloader
       Ctrl-C to stop server.
   ```


## Target Use Cases

* A user has run analyses in iPython Notebook and wants to easily make the
  results available on the web. The results are already contained
  in the notebook

* A user has analyses that need to be run regularly or on-demand, and
  the served notebooks are a way to easily generate that dynamic content.

* A user develops notebooks with extensive code, and needs a way to make
  them accessible to people who will be scared away or distracted by the code.

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

  * gunicorn nbserve:flask_app
  * nbserve
  * add it as a uswgi container to nginx, apache, etc, just like
    any other flask app.

## Development
### Releasing
```sh
# python setup.py register -r pypi
python setup.py sdist upload -r pypi
```

## Build Status
* Master: [![Build Status](https://travis-ci.org/robchambers/nbserve.svg?branch=master)](https://travis-ci.org/robchambers/nbserve)
* Develop: [![Build Status](https://travis-ci.org/robchambers/nbserve.svg?branch=develop)](https://travis-ci.org/robchambers/nbserve)

 