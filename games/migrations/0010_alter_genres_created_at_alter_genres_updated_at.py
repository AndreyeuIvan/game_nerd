# Generated by Django 4.0.2 on 2022-02-17 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0009_genres_checksum_genres_created_at_genres_slug_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="genres",
            name="created_at",
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="genres",
            name="updated_at",
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]