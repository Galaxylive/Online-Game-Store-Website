# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-18 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authtest', '0006_auto_20170128_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='salesCount',
            field=models.IntegerField(default=0),
        ),
    ]
