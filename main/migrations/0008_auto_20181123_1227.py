# Generated by Django 2.1.3 on 2018-11-23 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20181123_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='rodzaj',
            field=models.IntegerField(choices=[(0, 'Nieznany'), (4, 'Sci-fi'), (5, 'Thiller'), (1, 'Horror'), (3, 'Comedy'), (7, 'Document'), (2, 'Drama'), (6, 'Fantasy')], default=0),
        ),
    ]
