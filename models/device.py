from datetime import datetime

from sql_client.flask_app_client import sql_device_app

db = sql_device_app.db


class Device(db.Model):
    __tablename__ = "devices"
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    entered_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    removed = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    update_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<id {self.id}>"

    def serialize(self):
        return {
            "id": self.id,
            "platform": self.platform,
            "user_id": self.user_id,
            "entered_at": self.entered_at,
            "removed": self.removed,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
