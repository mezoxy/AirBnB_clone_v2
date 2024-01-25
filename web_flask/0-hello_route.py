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

if __name__ == '__main__':
    app.run(debug=True)
