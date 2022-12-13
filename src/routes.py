from flask import render_template

from . import app


@app.route("/healthcheck", strict_slashes=False)
def healthcheck():
    return 'I am alive and running!'

@app.route("/", strict_slashes=False)
def index():
    return render_template("index.html")