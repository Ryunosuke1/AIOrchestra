import discord

class DiscordAuth:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None

    async def get_access_token(self):
        url = "https://discord.com/api/v9/oauth2/token"
        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "scope": "bot application.commands"
        }
        async with discord.http.HTTPClient() as http:
            response = await http.post(url, form_data=data)
            if response.status == 200:
                self.access_token = response.json().get("access_token")
                return self.access_token
            else:
                raise Exception(f"Failed to get Discord access token: {response.text}")

    async def make_request(self, method, url, **kwargs):
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        async with discord.http.HTTPClient() as http:
            response = await http.request(method, url, headers=headers, **kwargs)
            return response
