from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user_model import User
from flask_app.models.sighting_model import Sighting


# ===============create page==============
@app.route("/sightings/new")
def new_sighting():
    logged_in_user = User.get_user(session["user_id"])
    return render_template("new_sighting.html", logged_in_user=logged_in_user)


# ===============create method==============
@app.route("/sightings/create", methods=["POST"])
def create_sighting():
    if not Sighting.val(request.form):
        return redirect("/sightings/new")

    Sighting.create_sighting(request.form)
    return redirect("/dash")


# ============= Get one sighting =============
@app.route("/sighting/<int:id>")
def get_sighting(id):
    sighting = Sighting.get_sighting(id)
    return render_template("sighting_card.html", sighting=sighting)


# ============= Update sighting Render=============
@app.route("/update/<int:id>")
def update_sighting(id):
    sighting = Sighting.get_sighting(id)
    return render_template("update_sighting.html", sighting=sighting)


# ============= Update sighting =============
@app.route("/sightings/update", methods=["POST"])
def update_sight():
    if not Sighting.val(request.form):
        return redirect(f"/update/{request.form['id']}")
    Sighting.update(request.form)
    return redirect("/dash")


# ============= Delete sighting =============
@app.route("/sightings/delete/<int:id>", methods=["POST"])
def delete_sighting(id):
    Sighting.delete({'sight_id': id})
    return redirect("/dash")