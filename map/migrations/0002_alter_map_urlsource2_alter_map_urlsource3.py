# Generated by Django 5.0.2 on 2024-04-17 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='urlSource2',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='map',
            name='urlSource3',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
    ]
