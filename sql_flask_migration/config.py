DSN = "postgresql://postgres:password@postgres:5432/act_device_api"


class Configuration:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DSN
    SQLALCHEMY_TRACK_MODIFICATIONS = True
