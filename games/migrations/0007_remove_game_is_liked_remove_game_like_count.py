# Generated by Django 4.0.2 on 2022-02-16 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_genres_platforms_twitter_game_rating_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='is_liked',
        ),
        migrations.RemoveField(
            model_name='game',
            name='like_count',
        ),
    ]