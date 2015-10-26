# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_menu_sid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='sid',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='sid',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
