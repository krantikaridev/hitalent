# Generated by Django 3.0.6 on 2022-03-24 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
