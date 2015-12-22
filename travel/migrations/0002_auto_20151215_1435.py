# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='province',
            new_name='province_name',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='coordinat',
        ),
        migrations.AddField(
            model_name='destination',
            name='latitude',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='longitude',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='tagline',
            field=models.CharField(default='', max_length=240),
            preserve_default=False,
        ),
    ]
