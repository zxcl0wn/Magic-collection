# Generated by Django 5.0.4 on 2024-04-21 12:06

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='colors',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=None),
        ),
    ]
