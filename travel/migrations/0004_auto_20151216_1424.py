# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_auto_20151215_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='province_name',
            field=models.ForeignKey(blank=True, to='travel.Province', null=True),
        ),
    ]
