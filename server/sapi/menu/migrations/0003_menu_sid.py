# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menu_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='sid',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
