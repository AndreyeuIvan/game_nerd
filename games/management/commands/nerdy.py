from django.core.management.base import BaseCommand

from games.service_igdb import IG, tw
from games.models import Twitter

from datetime import datetime
import json


class Command(BaseCommand):
    help = "Api handler and creatin fixtures"

    def get_all_obj(self, obj: list):
        try:
            objs = [int(x) for x in obj]
        except (TypeError, AttributeError):
            objs = ""
        return objs

    def get_tweet_id(self, name):
        tweet = tw.get_tweets(name)
        ids = []
        for t in tweet:
            new_tweet = Twitter(**t)
            new_tweet.save()
            ids.append(new_tweet.id)
        return ids

    def handle(self, *args, **options):
        date = datetime.now().strftime("%Y-%m-%d %H")
        igb_json = IG.get_games_list()
        my_format = [
            {
                "model": "games.game",
                "pk": game.get("id"),
                "fields": {
                    "name": game.get("name"),
                    "slug": game.get("slug"),
                    "summary": game.get("summary"),
                    "release_dates": game.get("release_dates"),
                    "rating": game.get("rating"),
                    "genres": self.get_all_obj(game.get("genres")),
                    "platforms": self.get_all_obj(game.get("platforms")),
                    "tweets": self.get_tweet_id(game.get("name")),
                },
            }
            for game in igb_json
        ]

        with open(f"fixture_{date}.json", "w") as file:
            json.dump(my_format, file)
