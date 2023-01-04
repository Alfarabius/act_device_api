from datetime import datetime

from sql_client.flask_app_client import sql_device_app

db = sql_device_app.db


class DeviceEvent(db.Model):
    __tablename__ = "device_events"
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, nullable=True)
    type = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    payload = db.Column(db.Json)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    update_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<id {self.id}>"
