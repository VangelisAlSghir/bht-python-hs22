# Generated by Django 4.1.5 on 2023-01-11 09:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Useradmin', '0003_defaultuser_date_of_brith_defaultuser_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultuser',
            name='date_of_brith',
            field=models.DateField(default=datetime.date(2003, 1, 11)),
        ),
    ]