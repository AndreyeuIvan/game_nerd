from platform import platform
from rest_framework import serializers
from games.models import Game


class GameSerializer(serializers.HyperlinkedModelSerializer):
    genres = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    platforms = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    tweets = serializers.SlugRelatedField(slug_field='text', read_only=True, many=True)
    
    class Meta:
        model = Game
        fields = ['name', 'slug', 'id', 'genres', 'platforms', 'tweets', 'likes']
        lookup_field = 'name'
