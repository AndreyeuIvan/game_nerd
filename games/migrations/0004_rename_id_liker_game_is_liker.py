# Generated by Django 4.0.2 on 2022-02-14 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0003_game_id_liker"),
    ]

    operations = [
        migrations.RenameField(
            model_name="game",
            old_name="id_liker",
            new_name="is_liker",
        ),
    ]