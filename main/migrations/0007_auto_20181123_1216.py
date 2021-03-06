# Generated by Django 2.1.3 on 2018-11-23 12:16

import annoying.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20181123_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='movie',
            field=annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.Movie'),
        ),
        migrations.AlterField(
            model_name='extrainfo',
            name='rodzaj',
            field=models.IntegerField(choices=[(6, 'Fantasy'), (3, 'Comedy'), (2, 'Drama'), (1, 'Horror'), (7, 'Document'), (5, 'Thiller'), (0, 'Nieznany'), (4, 'Sci-fi')], default=0),
        ),
    ]
