# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-21 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badgrsocialauth', '0002_saml2configuration_cached_metadata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saml2configuration',
            name='cached_metadata',
            field=models.TextField(blank=True, default='', help_text='If the XML is provided here we avoid making a network request to the metadata_conf_url.'),
        ),
        migrations.AlterField(
            model_name='saml2configuration',
            name='metadata_conf_url',
            field=models.URLField(help_text='The URL for the XML configuration for SAML2 flows. Get this from the Identity Provider Application.', verbose_name='Metadata Configuration URL'),
        ),
        migrations.AlterField(
            model_name='saml2configuration',
            name='slug',
            field=models.CharField(help_text='This slug must be prefixed with saml2.', max_length=32, unique=True),
        ),
    ]
