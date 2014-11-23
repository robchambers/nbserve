import flask
import nbserve
import os


flask_app = flask.Flask(nbserve.__progname__)

flask_app.config['DEBUG'] = True

from IPython.html.services.notebooks.filenbmanager import FileNotebookManager
from streamingexporter import StreamingRunningHTMLExporter

nbmanager = FileNotebookManager(notebook_dir='.')



def set_working_directory(path):
    if not os.path.exists(path):
        raise IOError('Path not found: %s' % os.path.abspath(path))
    nbmanager.notebook_dir = path

@flask_app.route('/')
def render_index():
    from jinja2 import Template
    template = Template("""<html>
    <body>
    <h2>Notebooks</h2>
    <ul>
        {% for notebook in notebooks %}
            <li><a href='{{ notebook.name }}'>{{notebook.name}}</a></li>
        {% endfor %}
    </ul>
    </body>
    </html>""")
    def notebooks():
        for nb in nbmanager.list_notebooks('.'):
            import time
            time.sleep(.5)
            print str(nb)
            yield nb
    return flask.Response(template.stream(notebooks=notebooks()))

@flask_app.route('/<nbname>/')
def render_page(nbname):



    if not nbmanager.notebook_exists(nbname):
        print "Notebook %s does not exist." % nbname
        flask.abort(404)

    print "Loading notebook %s" % nbname
    nbmanager.trust_notebook(nbname)
    nb = nbmanager.get_notebook(nbname)

    print "Exporting notebook"
    exporter = StreamingRunningHTMLExporter(
        #config=Config({'HTMLExporter':{'default_template':args.template}})
    )

    output, resources = exporter.from_notebook_node(nb['content'])
    print "Returning."
    return flask.Response(output)

if __name__ == "__main__":
    flask_app.run()
