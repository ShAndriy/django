# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-12 09:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customUserName', models.TextField()),
                ('customFirstName', models.TextField()),
                ('customLastName', models.TextField()),
                ('firstFood', models.TextField()),
                ('garnish', models.TextField()),
                ('salad', models.TextField()),
                ('meatDish', models.TextField()),
                ('fruits', models.TextField()),
                ('complex', models.TextField()),
                ('customDate', models.DateField()),
                ('dinnerDate', models.DateField()),
                ('customPrice', models.FloatField()),
            ],
            options={
                'db_table': 'customFood',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodName', models.TextField()),
                ('foodImage', models.TextField(default=None)),
            ],
            options={
                'db_table': 'food',
            },
        ),
        migrations.CreateModel(
            name='FoodDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodDay', models.TextField()),
                ('foodDayNumber', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'food_day',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.TextField()),
                ('categoryPrice', models.FloatField()),
            ],
            options={
                'db_table': 'menu',
            },
        ),
        migrations.AddField(
            model_name='food',
            name='foodCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dinner.Menu'),
        ),
        migrations.AddField(
            model_name='food',
            name='foodDay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dinner.FoodDay'),
        ),
    ]
