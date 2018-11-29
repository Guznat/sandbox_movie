# Generated by Django 2.1.3 on 2018-11-21 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(default='')),
                ('year', models.IntegerField(blank=True, null=True)),
                ('released', models.DateField(blank=True, null=True)),
                ('imdb_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='plakaty')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, default='', max_length=260)),
                ('stars', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('czas_trwnia', models.IntegerField(default=0)),
                ('rodzaj', models.IntegerField(choices=[(1, 'Horror'), (2, 'Drama'), (4, 'Sci-fi'), (0, 'Unknown'), (7, 'Document'), (5, 'Thiller'), (6, 'Fantasy'), (3, 'Comedy')], default=0)),
                ('movie', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Movie'),
        ),
    ]
