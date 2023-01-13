from flask_app_client import app, db
from models import Device, DeviceEvent

if __name__ == "__main__":
    print(f"{app, db, Device, DeviceEvent}")


@app.route("/")
def get_data():
    return "Hello, i`m sql orm app"
