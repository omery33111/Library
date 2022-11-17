import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS



# ---------- DATA BASE SETUP:

app = Flask(__name__)
app.url_map.strict_slashes = False
UPLOAD_FOLDER = 'UPLOAD_FOLDER'
app.config['SECRET_KEY'] = "Omer's Library"         # ALLOWS US TO USE FORMS NOT SAFE DEPLOYMENT. 
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, "Library_DATABASE")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)
Migrate(app, db)
CORS(app)

# -------------------------------------------------- #



# ---------- REGISTER BLUEPRINTS:

from project.core.views import core
from project.users.views import users
from project.books.views import books
from project.loans.views import loans

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(books)
app.register_blueprint(loans)



# ---------------------------------------------------------------------------------------------------- #