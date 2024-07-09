#!/usr/bin/python3
""" task 9 """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    return "This Project Sucks!"


@app.route('/states_list', strict_slashes=False)
def states_list():
    from models import storage
    from models.state import State

    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    from models import storage
    from models.state import State
    from models.city import City

    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    cities = storage.all(City).values()
    sorted_cities = sorted(cities, key=lambda city: city.name)
    return render_template('8-cities_by_states.html',
                           states=sorted_states,
                           cities=sorted_cities)


@app.teardown_appcontext
def teardown(exc):
    from models import storage
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
