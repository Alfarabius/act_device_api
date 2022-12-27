from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import DSN


class SQLDeviceAPP:
    def __init__(self, dsn: str):
        self.app = Flask(__name__)
        self.app.config["SQLALCHEMY_DATABASE_URI"] = dsn
        self.db = SQLAlchemy(self.app)


sql_device_app = SQLDeviceAPP(DSN)


if __name__ == "__main__":
    sql_device_app.app.run(debug=True)
