from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    import os.path
    return os.path.abspath('.')

if __name__ == "__main__":
    app.run()