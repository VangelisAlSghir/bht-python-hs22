# Generated by Django 4.1.1 on 2023-01-20 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0007_alter_movie_image_alter_movie_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
