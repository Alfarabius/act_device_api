from datetime import datetime

from flask import jsonify, request, send_from_directory
from flask_app_client import app, db
from flask_cors import cross_origin
from flask_swagger_ui import get_swaggerui_blueprint
from models import Device, DeviceEvent

from config import API_URL, SWAGGER_URL

if __name__ == "__main__":
    print(f"{app, db, Device, DeviceEvent}")


swagger_ui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={"app_name": "act-device-api"})

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


@app.route("/")
def index():
    return jsonify({"message": "Hello, i`m ActDeviceAPI"})


@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory("static", path)


@cross_origin()
@app.route("/api/v1/devices", methods=["POST"])
def create_device():
    if not request.is_json:
        return jsonify({"error": "The request payload is not in JSON format"})

    data = request.get_json()
    new_device = Device(user_id=data["user_id"], platform=data["platform"])

    db.session.add(new_device)
    db.session.commit()
    return jsonify({"message": f"device {new_device} has been created successfully."})


@cross_origin()
@app.route("/api/v1/devices/<device_id>", methods=["GET"])
def get_device(device_id):
    device = Device.query.get_or_404(device_id)
    response = Device.serialize(device)
    return jsonify({"device": response})


@cross_origin()
@app.route("/api/v1/devices/<device_id>", methods=["PATCH"])
def update_device(device_id):
    device = Device.query.get_or_404(device_id)

    if not request.is_json:
        return jsonify({"error": "The request payload is not in JSON format"})

    data = request.get_json()
    device.user_id = data["user_id"]
    device.platform = data["platform"]
    device.updated_at = datetime.utcnow

    db.session.add(device)
    db.session.commit()
    return jsonify({"message": f"{device} updated"})


@cross_origin()
@app.route("/api/v1/devices/<device_id>", methods=["DELETE"])
def delete_device(device_id):
    device = Device.query.get_or_404(device_id)

    db.session.delete(device)
    db.session.commit()
    return jsonify({"message": f"device {device} successfully deleted"})
