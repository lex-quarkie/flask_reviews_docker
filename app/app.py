import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.manage import parse_csv

class Config(object):
    postgres_user = os.getenv("POSTGRES_USER")
    postgres_password = os.getenv("POSTGRES_PASSWORD")
    postgres_db = os.getenv("POSTGRES_DB")
    database_url = (
        f"postgresql://{postgres_user}:{postgres_password}@postgres_db:5432/{postgres_db}"
    )

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", database_url)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def init_app():
    app = Flask(__name__)
    app.cli.add_command(parse_csv)
    app.config.from_object(Config)
    db.init_app(app)
    Migrate(app, db)

    return app

db = SQLAlchemy(session_options={"autoflush": False})
app = init_app()
