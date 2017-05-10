# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 14:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dinner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bascket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.TextField()),
                ('productCategory', models.TextField()),
                ('productPrice', models.FloatField()),
            ],
            options={
                'db_table': 'bascket',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('purchaseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dinner.Bascket')),
            ],
            options={
                'db_table': 'purchase',
            },
        ),
    ]
