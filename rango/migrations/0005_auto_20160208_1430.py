# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20160208_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='views',
            new_name='view',
        ),
    ]
