from datetime import datetime

from flask_app_client import db


class Device(db.Model):
    __tablename__ = "devices"

    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    entered_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    removed = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    update_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, platform, user_id):
        super().__init__()
        self.user_id = user_id
        self.platform = platform

    def __repr__(self):
        return f"<Device {self.platform} with id {self.id}>"

    @staticmethod
    def serialize(model):
        return {
            "id": model.id,
            "platform": model.platform,
            "user_id": model.user_id,
            "entered_at": model.entered_at,
            "removed": model.removed,
            "created_at": model.created_at,
            "update_at": model.update_at,
        }


class DeviceEvent(db.Model):
    __tablename__ = "device_events"

    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, nullable=True)
    type = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    payload = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    update_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return (
            f"id: {self.id}, device_id: {self.device_id}, "
            f"type: {self.type}, status: {self.status}, "
            f"payload: {self.payload}, created_at: {self.created_at}, "
            f"updated_at: {self.updated_at}"
        )
