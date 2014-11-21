from flask import Flask
from nb2web import render_nb
app = Flask(__name__)


@app.route('/')
def index():
    return render_nb("mocknb1.ipynb")

if __name__ == "__main__":
    app.run()