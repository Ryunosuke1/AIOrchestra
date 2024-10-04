import uuid

class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, user_id):
        session_id = str(uuid.uuid4())
        self.sessions[session_id] = {
            "user_id": user_id,
            "created_at": datetime.datetime.now()
        }
        return session_id

    def get_user_by_session(self, session_id):
        return self.sessions.get(session_id, {}).get("user_id")

    def invalidate_session(self, session_id):
        if session_id in self.sessions:
            del self.sessions[session_id]
