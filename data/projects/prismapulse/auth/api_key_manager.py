import hashlib
import time

class ApiKeyManager:
    def __init__(self):
        self.api_keys = {}

    def generate_api_key(self, user_id):
        key = str(time.time()) + user_id
        hash_object = hashlib.sha256(key.encode())
        api_key = hash_object.hexdigest()
        self.api_keys[api_key] = {
            "user_id": user_id,
            "created_at": time.time(),
            "expires_at": time.time() + 3600  # Expires in 1 hour
        }
        return api_key

    def is_api_key_valid(self, api_key):
        if api_key in self.api_keys:
            if self.api_keys[api_key]["expires_at"] > time.time():
                return True
        return False

    def get_user_by_api_key(self, api_key):
        return self.api_keys.get(api_key, {}).get("user_id")
