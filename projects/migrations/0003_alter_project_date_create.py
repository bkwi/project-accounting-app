# Generated by Django 4.1.4 on 2023-01-26 19:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_date_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 26, 20, 25, 50, 351003)),
        ),
    ]
