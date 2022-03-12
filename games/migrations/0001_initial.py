# Generated by Django 4.0.2 on 2022-02-23 21:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.CharField(max_length=250)),
                ("name", models.CharField(max_length=250)),
                ("slug", models.CharField(max_length=250)),
                ("updated_at", models.CharField(max_length=250)),
                ("url", models.URLField()),
                ("checksum", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Platform",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Twitter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.CharField(max_length=500)),
                ("_id", models.CharField(max_length=250)),
                ("created_at", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=500)),
                ("slug", models.SlugField(blank=True, max_length=500, unique=True)),
                ("summary", models.CharField(blank=True, max_length=1500, null=True)),
                (
                    "release_dates",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("rating", models.BigIntegerField(blank=True, null=True)),
                (
                    "genres",
                    models.ManyToManyField(related_name="genres", to="games.Genre"),
                ),
                (
                    "likes",
                    models.ManyToManyField(
                        blank=True, related_name="like", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "platforms",
                    models.ManyToManyField(
                        related_name="platforms", to="games.Platform"
                    ),
                ),
                (
                    "tweets",
                    models.ManyToManyField(related_name="tweets", to="games.Twitter"),
                ),
            ],
        ),
    ]
