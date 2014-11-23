import flask
import nbserve
import os


flask_app = flask.Flask(nbserve.__progname__)
flask_app.config['DEBUG'] = True

#############
# Initialize some IPython and RunIPy services.
from IPython.html.services.notebooks.filenbmanager import FileNotebookManager
nbmanager = FileNotebookManager(notebook_dir='.')
##
# This thread initializes a notebook runner, so that it's
# ready to go on first page access.
runner = None
import threading
def make_notebook_runner():
    global runner
    from runipy.notebook_runner import NotebookRunner
    runner = NotebookRunner(None)
    print "Runner is ready."
make_notebook_runner_thread = threading.Thread(target=make_notebook_runner)
make_notebook_runner_thread.start()


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
    global runner
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
            if runner is None:
                make_notebook_runner_thread.join()

            # Do as complete of a reset of the kernel as we can.
            # Unfortunately, this doesn't really do a 'hard' reset
            # of any modules...
            class ResetCell(dict):
                """Simulates just enough of a notebook cell to get this
                '%reset -f' cell executed using the existing runipy
                 machinery."""
                input = "%reset -f"
            runner.run_cell(ResetCell())
            runner.nb = nb['content']
            print "Running notebook"
            runner.run_notebook(skip_exceptions=True)
            break
        except Empty as e:
            print "WARNING: Empty bug happened."
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
