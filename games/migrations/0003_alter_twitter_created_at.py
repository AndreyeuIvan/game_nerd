# Generated by Django 4.0.2 on 2022-02-23 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
        ("games", "0002_alter_twitter__id"),
=======
        ('games', '0002_alter_twitter__id'),
>>>>>>> e3c9e71feb93abe7823ccc85314b8fcbbf0042f9
    ]

    operations = [
        migrations.AlterField(
<<<<<<< HEAD
            model_name="twitter",
            name="created_at",
=======
            model_name='twitter',
            name='created_at',
>>>>>>> e3c9e71feb93abe7823ccc85314b8fcbbf0042f9
            field=models.CharField(max_length=300),
        ),
    ]
