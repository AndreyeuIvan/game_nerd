from ast import List
from requests import post
import json


class MyAuth:
    """
    Main goal is get token, in order to dos, we need credentilas(client_id, secret
    """

    def __init__(self, secret: str, client_id: str, url: str):
        self.secret = secret
        self.client_id = client_id
        self.url = url

    def get_token(self, grant_type: dict):
        """
        1. Create post request
        2. Provide cretentials and grant_type(applicable for twitch
        """
        auth_body = {
            "client_id": self.client_id,
            "client_secret": self.secret,
        }
        auth_body = auth_body | grant_type
        auth_response = post(self.url, auth_body)
        return auth_response.json()


# igdb
URL_TWITCH = "https://id.twitch.tv/oauth2/token"
client_secret_twitch = "hz9akahuzsa418xmflcfqrpdoqvokq"
client_id_twitch = "txzxbs4vpf2y9scp1045n6oyzqzwxm"
twitch_required = {"grant_type": "client_credentials"}

# getting token
twitch = MyAuth(client_secret_twitch, client_id_twitch, URL_TWITCH)
token_twitch = twitch.get_token(twitch_required)["access_token"]

IGB_URL = "https://api.igdb.com/v4/"


class IGDBWrapper:
    def __init__(self, client_id: str, auth_token: str):
        self.client_id = client_id
        self.auth_token = auth_token

    def api_request(self, endpoint: str, query: str):
        """
        Takes an endpoint and the Apicalypse query and returns the api response as a byte string.
        """
        url = IGDBWrapper._build_url(endpoint)
        params = self._compose_request(query)
        # import pdb; pdb.set_trace()
        response = post(url, **params)
        response.raise_for_status()
        return response.content

    @staticmethod
    def _build_url(endpoint: str = ""):
        """
        Creatin an url by passing enpoint and api_url"""
        return f"{IGB_URL}{endpoint}"

    def _compose_request(self, query: str):
        if not query:
            raise Exception("No query provided!")
        request_params = {
            "headers": {
                "Client-ID": self.client_id,
                "Authorization": (f"Bearer {self.auth_token}"),
            }
        }
        if isinstance(query, str):
            request_params["data"] = query
            return request_params
        raise TypeError("Incorrect type of argument query")

    def to_json(self, games: bytes):
        """
        Handler for createing json objects from bytes
        """
        return json.loads(games)

    def get_all(self):
        """
        1. Return all, but it will be 10 maximum.
        2. Wrape it into variable games.
        3. Trasform into json obj.
        """
        query = "fields *;"
        endpoint = "games"
        games = self.api_request(endpoint, query)
        games_json = self.to_json(games)
        return games_json

    def get_genre(self, id: List):
        id = tuple(id)
        query = f"fields name ; where id={id};"
        endpoint = "genres"
        genres_bytes = self.api_request(endpoint, query)
        genres_json = self.to_json(genres_bytes)
        new_genres = [x["name"] for x in genres_json]
        return new_genres

    def get_by_id(self, id: int):
        """
        1. Return game, according to provided id.
        2. Wrape it into variable games.
        3. Trasform into json obj.
        """
        query = f"fields * ; where id={id};"
        endpoint = "games"
        games = self.api_request(endpoint, query)
        games_json = self.to_json(games)
        # import pdb; pdb.set_trace()
        genres = self.get_genre(games_json[0]["genres"])
        games_json[0]["genres"] = genres
        return games_json


IG = IGDBWrapper(client_id_twitch, token_twitch)
# import pdb; pdb.set_trace()

# twitter
URL_TWITTER = "https://api.twitter.com/2/users/by/username/"
URL_TWITTER_AUTH = "https://api.twitter.com/oauth2/token"
twitter_required = {"grant_type": "client_credentials"}
API_KEY_TWITTER = ""
API_SECRET_KEY = ""
