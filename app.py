# 1. import dependencies
from flask import Flask, json, jsonify

import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect, distinct, desc
from sqlalchemy.sql import label

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo=False)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
Measurement = Base.classes.measurement
Stations = Base.classes.station


# 2. create an app, being sure to pass __name__
app = Flask(__name__)

# =========================
# @app.route("/api/v1.0/justice-league")
# def justice_league():
  #  """Return the justice league data as json"""
#
   # return jsonify(justice_league_members)
# ==============================================

# 3.0 Define what to do when a user hits the index route
# list all routes that are available
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

# 3.1
#  * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
#  * Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation")
def precip():
    print("Server received request for 'precipipation' page...")
    # Create our session (link) from Python to the DB
    session = Session(engine)

    precip_output = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= dt.date(2016, 8, 23)).all()
          
    session.close()

    #precip_info = list(np.ravel(precip_output))

    precip_dict = {}

    for row in precip_output:
        precip_dict[row[0]]=row[1]

    #return "Welcome to the Preicipation page! Here are the precipitation data for 24 August 2016 to 24 August 2017"
    return jsonify(precip_dict)

# 3.2
#   * Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    print("Server received request for 'stations' page...")
    
    session = Session(engine)

    station_output = session.query(Stations.station, Stations.name).all()

    station_dict = {}
    for row in station_output:
        station_dict[row[0]]=row[1]

    return jsonify(station_dict)
    
    # return "Welcome to the Stations page!"

# 3.3
#   * Query the dates and temperature observations of the most active station for the last year of data.
# * Return a JSON list of temperature observations (TOBS) for the previous year.
@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for 'temperature' page...")
    
    session = Session(engine)

    active_station = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= dt.date(2016, 8, 23), Measurement.station == "USC00519281").\
        order_by(Measurement.tobs).all()

    active_dict ={}
    for row in active_station:
        active_dict[row[0]]=row[1]
    
    return jsonify(active_dict)
    # return "Welcome to the Observed Temperature page!"

# 3.4
#  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
#  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
@app.route("/api/v1.0/<start>")
def temp_search1(start):
    print("Server received request for 'temperature search' page...")
    return "Type in a start date for your temperature search"

# 3.5
#  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
@app.route("/api/v1.0/<start>/<end>")
def temp_search2(start, end):
    print("Server received request for 'temperature search' page...")
    return "Type in start and end dates for your temperature search"

if __name__ == "__main__":
    app.run(debug=True)