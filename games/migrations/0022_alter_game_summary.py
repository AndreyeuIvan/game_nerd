# Generated by Django 4.0.2 on 2022-02-17 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0021_alter_game_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='summary',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
    ]