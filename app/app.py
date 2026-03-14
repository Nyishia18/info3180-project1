from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from flask import render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://project1:info3180project1@localhost/propertydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# File upload configuration
UPLOAD_FOLDER = os.path.join('app', 'static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # creates folder if it doesn't exist

# Initialize DB and Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)