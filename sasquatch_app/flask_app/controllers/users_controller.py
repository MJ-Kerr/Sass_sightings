from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models import user_model
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)