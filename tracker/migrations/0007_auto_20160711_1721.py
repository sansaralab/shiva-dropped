# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 17:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_auto_20160711_1721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personcontact',
            old_name='info_type',
            new_name='contact_type',
        ),
        migrations.RenameField(
            model_name='personcontact',
            old_name='info_value',
            new_name='contact_value',
        ),
        migrations.AlterUniqueTogether(
            name='personcontact',
            unique_together=set([('person', 'contact_type', 'contact_value')]),
        ),
    ]
