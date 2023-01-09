# Generated by Django 4.1.4 on 2023-01-09 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0003_movie_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.FileField(blank=True, upload_to='media/movies/images/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='pdf',
            field=models.FileField(blank=True, upload_to='media/movies/pdf/'),
        ),
    ]
