# Generated by Django 4.2 on 2023-04-26 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_movies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='imdbid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='movies',
            name='imdbscore',
            field=models.FloatField(default=-1),
        ),
    ]
