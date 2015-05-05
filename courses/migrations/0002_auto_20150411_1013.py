# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='assistant',
            field=models.ForeignKey(related_name='assistant', blank=True, to='coaches.Coach', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(related_name='instructor', blank=True, to='coaches.Coach', null=True),
            preserve_default=True,
        ),
    ]
