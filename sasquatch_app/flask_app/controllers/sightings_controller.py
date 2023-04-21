from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user_model import User
from flask_app.models import sighting_model


# ===============create page==============
@app.route("/sightings/new")
def new_sighting():
    return render_template("new_sighting.html")