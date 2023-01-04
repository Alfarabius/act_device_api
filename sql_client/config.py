DSN = "postgresql+psycopg2://docker:docker@localhost:5432/act_device_api"


class Configuration:
    DEBUG = True
    SECRET_KEY = "this-really-needs-to-be-changed"
    SQLALCHEMY_DATABASE_URI = DSN
    SQLALCHEMY_TRACK_MODIFICATIONS = True
