# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-07 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_name', models.CharField(blank=True, max_length=200, null=True)),
                ('fed_tax_ID', models.IntegerField(blank=True, null=True)),
                ('address_line_one', models.CharField(blank=True, max_length=2000, null=True)),
                ('address_line_two', models.CharField(blank=True, max_length=2000, null=True)),
                ('address_city', models.CharField(blank=True, max_length=2000, null=True)),
                ('address_state', models.CharField(blank=True, max_length=2000, null=True)),
                ('address_zip', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]