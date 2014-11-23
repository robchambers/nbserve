import flask
import nbserve
import os


flask_app = flask.Flask(nbserve.__progname__)

flask_app.config['DEBUG'] = True

from IPython.html.services.notebooks.filenbmanager import FileNotebookManager


nbmanager = FileNotebookManager(notebook_dir='.')

def set_working_directory(path):
    if not os.path.exists(path):
        raise IOError('Path not found: %s' % os.path.abspath(path))
    nbmanager.notebook_dir = path

@flask_app.route('/')
def render_index():
    template = """<html>
    <body>
    <h2>Notebooks</h2>
    <ul>
        {% for notebook in notebooks %}
            <li><a href='{{ notebook.name }}'>{{notebook.name}}</a></li>
        {% endfor %}
    </ul>
    </body>
    </html>"""
    return flask.render_template_string(template, notebooks=nbmanager.list_notebooks('.'))

@flask_app.route('/<nbname>/')
def render_page(nbname):
    from runipy.notebook_runner import NotebookRunner
    from IPython.nbconvert.exporters.html import HTMLExporter

    if not nbmanager.notebook_exists(nbname):
        print "Notebook %s does not exist." % nbname
        flask.abort(404)

    print "Loading notebook %s" % nbname
    nbmanager.trust_notebook(nbname)
    nb = nbmanager.get_notebook(nbname)
    print "Making runner..."''

    # This is an ugly little bit to deal with a sporadic
    #  'queue empty' bug in iPython that only seems to
    #  happen on the integration servers...
    #  see https://github.com/paulgb/runipy/issues/36
    N_RUN_RETRIES = 4
    from Queue import Empty
    for i in range(N_RUN_RETRIES):
        try:
            runner = NotebookRunner(nb['content'])
            print "Running notebook"
            runner.run_notebook()
            break
        except Empty as e:
            if i >= (N_RUN_RETRIES - 1):
                raise

    print "Exporting notebook"
    exporter = HTMLExporter(
        #config=Config({'HTMLExporter':{'default_template':args.template}})
    )
    output, resources = exporter.from_notebook_node(runner.nb)
    print "Returning."
    return output

if __name__ == "__main__":
    flask_app.run()
