#in order to run, type 'python -m flask run' in the command line

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"


if __name__ == '__main__':
    app.run()