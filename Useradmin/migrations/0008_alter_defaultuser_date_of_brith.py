# Generated by Django 4.1.5 on 2023-01-18 09:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Useradmin', '0007_alter_defaultuser_date_of_brith'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultuser',
            name='date_of_brith',
            field=models.DateField(default=datetime.date(2003, 1, 18)),
        ),
    ]
