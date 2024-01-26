#!/usr/bin/python3
"""The module: 0-hello_route"""


from flask import Flask as f


app = f(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hbn():
    """
        hbn: A function tha returns Hello HBNB!
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def Hbn():
    """
        Hbn: A function that returns HBNB
    """
    return "HBNB"


@app.route("/c/<text>")
def CisFun(text=None):
    """
        cisFun: A function that display “C ” followed by the text
    """
    return "C {}".format(" ".join(text.split("_")))


@app.route("/python")
@app.route("/python/<text>")
def py(text="is cool"):
    """
        py: A function that display Python followed by the text
    """
    return "Python {}".format(" ".join(text.split("_")))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
