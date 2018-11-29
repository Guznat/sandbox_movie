# Generated by Django 2.1.3 on 2018-11-23 13:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20181123_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='extrainfo',
            name='rodzaj',
            field=models.IntegerField(choices=[(6, 'Fantasy'), (4, 'Sci-fi'), (1, 'Horror'), (3, 'Comedy'), (2, 'Drama'), (5, 'Thiller'), (0, 'Nieznany'), (7, 'Document')], default=0),
        ),
    ]