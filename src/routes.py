from . import app


@app.route("/healthcheck", strict_slashes=False)
def healthcheck():
    return 'I am alive and running!'

