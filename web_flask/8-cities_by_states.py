#!/usr/bin/python3
"""The module: 0-hello_route"""


from flask import Flask as f
from models import storage
from models.state import State
from flask import render_template
from os import getenv


app = f(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def states():
    """A function that returns all the states"""
    list_states = sorted(list(storage.all(State).values()), key=lambda x: x.name if x.name)
    dic_city = {}
    for state in list_states:
        dic_city[state] = sorted([city for city in state.cities], key=lambda x: x.name if x.name)
    return render_template('8-cities_by_states.html', dic=dic_city)


@app.teardown_appcontext
def teardown_db(exception):
    """
        A function to close connection
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
