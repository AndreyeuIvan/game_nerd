import requests
from requests.structures import CaseInsensitiveDict
import json
import re
import environ
import games.settings as _

env = environ.Env()
environ.Env.read_env()


class MyAuth:
    """
    Main goal is get token, in order to dos, we need credentilas(client_id, secret
    """

    def __init__(self, secret: str, client_id: str, url: str):
        self.secret = secret
        self.client_id = client_id
        self.url = url

    def get_token_twitch(self, grant_type: dict):
        """
        1. Create post request
        2. Provide cretentials and grant_type(applicable for twitch
        """
        auth_body = {
            "client_id": self.client_id,
            "client_secret": self.secret,
        }
        auth_body = auth_body | grant_type
        auth_response = requests.post(self.url, auth_body)
        return auth_response.json()

    def get_token_twitter(self, hash: str):
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        headers["Authorization"] = f"Basic {hash}"
        data = "grant_type=client_credentials"
        auth_response = requests.post(URL_TWITTER_AUTH, headers=headers, data=data)
        return auth_response


# igdb
URL_TWITCH = "https://id.twitch.tv/oauth2/token"
client_secret_twitch = env("client_secret_twitch")
client_id_twitch = env("client_id_twitch")
twitch_required = {"grant_type": "client_credentials"}

# getting token
twitch = MyAuth(client_secret_twitch, client_id_twitch, URL_TWITCH)
token_twitch = twitch.get_token_twitch(twitch_required)["access_token"]

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
        response = requests.post(url, **params)
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

    def get_games_list(self):
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

    def get_genre(self, id: list):
        id = tuple(id)
        query = f"fields name ; where id={id};"
        endpoint = "genres"
        genres_bytes = self.api_request(endpoint, query)
        genres_json = self.to_json(genres_bytes)
        new_genres = [x["name"] for x in genres_json]
        return new_genres

    def get_game_by_id(self, id: int):
        """
        1. Return game, according to provided id.
        2. Wrape it into variable games.
        3. Trasform into json obj.
        """
        query = f"fields * ; where id={id};"
        endpoint = "games"
        games = self.api_request(endpoint, query)
        games_json = self.to_json(games)
        genres = self.get_genre(games_json[0]["genres"])
        games_json[0]["genres"] = genres
        return games_json


IG = IGDBWrapper(client_id_twitch, token_twitch)


# twitter
URL_TWITTER_AUTH = "https://api.twitter.com/oauth2/token"
API_KEY_TWITTER = env("API_KEY_TWITTER")
API_SECRET_KEY = env("API_SECRET_KEY")
BEARER_TOKEN = env("BEARER_TOKEN")
HASH = env("HASH")

# get tokken for twitter
auth_tweet = MyAuth(
    secret=API_SECRET_KEY, client_id=API_KEY_TWITTER, url=URL_TWITTER_AUTH
).get_token_twitter(HASH)
token_twitter = auth_tweet.json()["access_token"]
print(auth_tweet.status_code)


URL_TWITTER_SEARCH = "https://api.twitter.com/2/tweets/search/recent"


class TwitterWrapper:
    def __init__(self, token: str):
        self.token = token

    @staticmethod
    def _build_url(query: str):
        """
        Creating an url by concatinating url and query
        """
        return f"{URL_TWITTER_SEARCH}{query}"

    def api_request(self, game_name: str):
        """
        Create request to api
        """
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        headers["Authorization"] = f"Bearer {self.token}"
        query = f"?query={game_name}%20&tweet.fields=created_at,text"
        response = requests.get(self._build_url(query), headers=headers)
        return response.json()

    def get_tweets(self, game_name: str):
        """
        Convert answer into a list
        """
        game_name = game_name.replace(" ", "")
        re_game = re.sub("[^a-zA-Z0-9 \n\.]", "", game_name)
        try:
            list_of_tweets = self.api_request(re_game)["data"]
        except:
            list_of_tweets = ""
        return list_of_tweets


tw = TwitterWrapper(token_twitter)
