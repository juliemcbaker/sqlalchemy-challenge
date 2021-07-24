# 1. import Flask
from flask import Flask, jsonify

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# 2. create an app, being sure to pass __name__
app = Flask(__name__)

# =========================
# @app.route("/api/v1.0/justice-league")
# def justice_league():
  #  """Return the justice league data as json"""
#
   # return jsonify(justice_league_members)
# ==============================================

# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
        f"Welcome to Climate App Home Page<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )
# list all routes that are available


@app.route("/api/v1.0/precipitation")
def precip():
    print("Server received request for 'precipipation' page...")
    return "Welcome to the Preicipation page!"
#  * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
#  * Return the JSON representation of your dictionary.

@app.route("/api/v1.0/stations")
def stations():
    print("Server received request for 'stations' page...")
    return "Welcome to the Stations page!"
#   * Return a JSON list of stations from the dataset.


@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for 'temperature' page...")
    return "Welcome to the Observed Temperature page!"
#   * Query the dates and temperature observations of the most active station for the last year of data.
# * Return a JSON list of temperature observations (TOBS) for the previous year.

@app.route("/api/v1.0/<start>")
def temp_search1(start):
    print("Server received request for 'temperature search' page...")
    return "Type in a start date for your temperature search"

#  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
#  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
#  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
@app.route("/api/v1.0/<start>/<end>")
def temp_search2(start, end):
    print("Server received request for 'temperature search' page...")
    return "Type in start and end dates for your temperature search"

if __name__ == "__main__":
    app.run(debug=True)