# Generated by Django 2.1.2 on 2019-04-06 20:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distrochooser', '0024_auto_20190406_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='distribution',
            name='identifier',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='usersession',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 6, 22, 18, 46, 304387)),
        ),
    ]
