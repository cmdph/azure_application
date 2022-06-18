import flask
import json
from flask import Flask, request, render_template

from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



# Running the api
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    