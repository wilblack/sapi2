# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='source',
            field=models.CharField(default=b'local', max_length=25, choices=[(b'local', b'User Defined'), (b'mmjmenu', b'MMJ Menu'), (b'biotrack', b'Bio Tracker')]),
        ),
    ]
