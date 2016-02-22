# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 08:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_redirects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='redirecttranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'redirect Translation'},
        ),
        migrations.AlterField(
            model_name='redirect',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aldryn_redirects_redirect_set', to='sites.Site'),
        ),
        migrations.AlterField(
            model_name='redirecttranslation',
            name='language_code',
            field=models.CharField(db_index=True, max_length=15, verbose_name='Language'),
        ),
    ]
