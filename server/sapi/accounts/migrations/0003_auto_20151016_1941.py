# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20151011_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField(null=True, blank=True)),
                ('attrs', jsonfield.fields.JSONField(default={}, help_text=b'A JSON object to hold general settings for this Org')),
            ],
        ),
        migrations.AlterField(
            model_name='org',
            name='slug',
            field=models.SlugField(max_length=254, unique=True, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='org',
            field=models.ForeignKey(to='accounts.Org'),
        ),
    ]
