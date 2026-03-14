from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

# Initialize the Flask app with the template folder specified
app = Flask(__name__, template_folder='templates')

# Configuration settings
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://project1:info3180project1@localhost/propertydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
migrate.init_app(app, db)

# Import routes and models at the bottom to avoid circular imports
from . import views
from . import models