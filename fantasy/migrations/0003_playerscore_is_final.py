# Generated by Django 4.0.3 on 2022-05-01 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantasy', '0002_player_tournament_tournamentstage_playerscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerscore',
            name='is_final',
            field=models.BooleanField(default=False),
        ),
    ]