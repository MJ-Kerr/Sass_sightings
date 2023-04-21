from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash 
import re
EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')