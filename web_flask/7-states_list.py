#!/usr/bin/python3
"""The module: 0-hello_route"""


from flask import Flask as f
from models import storage
from models.state import State
from flask import render_template


app = f(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states():
    """A function that returns all the states"""
    dic = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template('7-states_list.html', dic=dic)


@app.teardown_appcontext
def closeDb(exception):
    """
        A function to close connection
    """
    storage.close()


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


@app.route('/number/<int:n>')
def num(n):
    """
        num: A function that display n is a number” only if n is an integer
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def num_tem(n):
    """
        num_tem: A function that display n is a number” only if n is an integer
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_even(n):
    """
        odd_even: display a HTML page only if n is an integer
                    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
