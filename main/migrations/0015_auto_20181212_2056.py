# Generated by Django 2.1.3 on 2018-12-12 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20181129_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='rodzaj',
            field=models.IntegerField(choices=[(3, 'Comedy'), (1, 'Horror'), (4, 'Sci-fi'), (5, 'Thiller'), (6, 'Fantasy'), (2, 'Drama'), (0, 'Nieznany'), (7, 'Document')], default=0),
        ),
    ]