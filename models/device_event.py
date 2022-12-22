class Device:
    def __init__(self, device_id, platform, user_id, entered_at, removed, created_at, update_at):
        self.id = device_id
        self.platform = platform
        self.user_id = user_id
        self.entered_at = entered_at
        self.removed = removed
        self.created_at = created_at
        self.updated_at = update_at

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
