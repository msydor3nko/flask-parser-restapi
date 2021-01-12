from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config


# app init and setup
app = Flask(__name__)
app.config.from_object(Config)

# database init and setup
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from api import routes, models
