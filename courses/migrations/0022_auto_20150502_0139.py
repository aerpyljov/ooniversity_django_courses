# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0021_auto_20150413_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='assistant',
            field=models.ForeignKey(related_name='assistant', verbose_name='\u0410\u0441\u0441\u0438\u0441\u0442\u0435\u043d\u0442', blank=True, to='coaches.Coach', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='coach',
            field=models.ForeignKey(related_name='coach', verbose_name='\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c', blank=True, to='coaches.Coach', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='course_title',
            field=models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0443\u0440\u0441\u0430'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='short_description',
            field=models.CharField(max_length=225, verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='consecutive_number',
            field=models.PositiveIntegerField(verbose_name='\u2116 \u0437\u0430\u043d\u044f\u0442\u0438\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(verbose_name='\u041a\u0443\u0440\u0441', to='courses.Course'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='desription',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='theme',
            field=models.CharField(max_length=255, verbose_name='\u0422\u0435\u043c\u0430'),
            preserve_default=True,
        ),
    ]