from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Configuration
from datetime import datetime


class SQLDeviceAPP:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config.from_object(Configuration)
        self.db = SQLAlchemy(self.app)
        self.migrate = Migrate()

        with self.app.app_context():
            self.migrate.init_app(self.app, self.db)


sql_device_app = SQLDeviceAPP()
app = sql_device_app.app  # for flask db command, doesn't work without it
db = sql_device_app.db
