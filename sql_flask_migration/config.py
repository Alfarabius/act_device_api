DSN = "postgresql://postgres:password@postgres:5432/act_device_api"
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"


class Configuration:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DSN
    SQLALCHEMY_TRACK_MODIFICATIONS = True
