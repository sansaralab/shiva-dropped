# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-15 20:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0010_auto_20160714_1810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trigger',
            old_name='action_type',
            new_name='reaction_side',
        ),
    ]