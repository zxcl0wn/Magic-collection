# Generated by Django 5.0.4 on 2024-04-21 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0002_alter_card_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='colors',
            field=models.TextField(null=True),
        ),
    ]