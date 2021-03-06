# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-25 13:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_received', to='products.Product'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]
