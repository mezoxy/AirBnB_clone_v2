#!/usr/bin/python3
"""The module: 0-hello_route"""


from flask import Flask as f
from models import storage
from models.state import State
from flask import render_template


app = f(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def states():
    """A function that returns all the states"""
    dic = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template('7-states_list.html', dic=dic)


@app.teardown_appcontext
def teardown_db(exception):
    """
        A function to close connection
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
