import json
from django.core.management.base import BaseCommand

from games.service_igdb import IG

from datetime import datetime


class Command(BaseCommand):
    help = 'Api handler and creatin fixtures'

    def handle(self, *args, **options):
        date = datetime.now().strftime('%Y-%m-%d %H')
        igb_json = IG.get_games_list()
        dir(igb_json)
        my_format = []
        for i in igb_json:
            my_format += [{
                    "model": "games.game",
                    "pk": i.get('id'),
                    "fields": {
                        "name": i.get('name'),
                        "slug": i.get('slug'),
                        "summary": i.get('summary'),
                        "release_dates": i.get('release_dates'),
                        "rating": i.get('rating'),
                        "genres": i.get('genres'),
                        "platforms": i.get('platforms'),
                        "tweets": 1,
                        "likes": [
                            1
                        ]
                    }
                }
            ]
        #import pdb;pdb.set_trace()
        with open(f'fixture_{date}.json', 'w') as file:
            json.dump(my_format, file)
