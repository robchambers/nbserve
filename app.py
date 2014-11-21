import flask, glob
from nb2web import render_nb
app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def render_index():
    nb_paths = glob.glob('*.ipynb')

    template = """<html>
    <body>
    <h2>Notebooks</h2>
    <ul>
        {% for nb_path in nb_paths %}
            <li><a href='{{ nb_path }}'>{{nb_path}}</a></li>
        {% endfor %}
    </ul>
    </body>
    </html>"""
    return flask.render_template_string(template, nb_paths=nb_paths)

@app.route('/<nbpath>/')
def render_page(nbpath):
    return render_nb(nbpath)

if __name__ == "__main__":
    app.run()
