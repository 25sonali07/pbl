# Generated by Django 3.0.3 on 2020-10-03 08:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diabetes',
            name='id',
        ),
        migrations.AddField(
            model_name='diabetes',
            name='sno',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diabetes',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='heart',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]