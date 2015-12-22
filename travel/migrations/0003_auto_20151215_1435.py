# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_auto_20151215_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='tagline',
            field=models.CharField(max_length=240, null=True, blank=True),
        ),
    ]
