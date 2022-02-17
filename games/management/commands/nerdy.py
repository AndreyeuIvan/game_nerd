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
        my_format = []
        for i in igb_json:
            my_format += [
                {
                    "model": "games.game",
                    "pk": i.get("id"),
                    "fields": {
                        "name": i.get("name"),
                        "slug": i.get("slug"),
                        "summary": i.get("summary"),
                        "release_dates": i.get("release_dates"),
                        "rating": i.get("rating"),
                        "genres": self.get_all_obj(i.get("genres")),
                        "platforms": self.get_all_obj(i.get("platforms")),
                        "tweets": self.get_tweet_id(i.get("name")),
                    },
                }
            ]
        with open(f"fixture_{date}.json", "w") as file:
            json.dump(my_format, file)
