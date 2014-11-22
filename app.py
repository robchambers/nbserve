import flask
from nbserve import render_nb
app = flask.Flask(__name__)
app.config['DEBUG'] = True

from IPython.html.services.notebooks.filenbmanager import FileNotebookManager


nbmanager = FileNotebookManager(notebook_dir='.')

@app.route('/')
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

@app.route('/<nbname>/')
def render_page(nbname):
    from runipy.notebook_runner import NotebookRunner
    from IPython.nbconvert.exporters.html import HTMLExporter
    from IPython.nbformat.current import to_notebook_json

    if not nbmanager.notebook_exists(nbname):
        print "Notebook %s does not exist." % nbname
        flask.abort(404)

    print "Loading notebook %s" % nbname
    nb  = nbmanager.get_notebook(nbname)
    print "Making runner..."
    runner = NotebookRunner(nb['content'])
    print "Running notebook"
    runner.run_notebook()
    print "Exporting notebook"
    exporter = HTMLExporter(
        #config=Config({'HTMLExporter':{'default_template':args.template}})
    )
    output, resources = exporter.from_notebook_node(runner.nb)
    print "Returning."
    return output

if __name__ == "__main__":
    app.run()
