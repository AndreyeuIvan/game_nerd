# Generated by Django 4.0.2 on 2022-02-23 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0002_alter_twitter__id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="twitter",
            name="created_at",
            field=models.CharField(max_length=300),
        ),
    ]
