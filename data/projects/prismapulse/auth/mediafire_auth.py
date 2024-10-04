import requests

class MediafireAuth:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None

    def get_access_token(self):
        url = "https://api.mediafire.com/oauth2/token"
        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            self.access_token = response.json().get("access_token")
            return self.access_token
        else:
            raise Exception(f"Failed to get Mediafire access token: {response.text}")

    def make_request(self, method, url, **kwargs):
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        response = requests.request(method, url, headers=headers, **kwargs)
        return response
