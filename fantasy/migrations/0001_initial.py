# Generated by Django 4.0.3 on 2022-04-02 12:50

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('twitter_url', models.URLField(blank=True)),
                ('twitch_url', models.URLField(blank=True)),
            ],
        ),
    ]