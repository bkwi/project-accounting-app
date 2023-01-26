# Generated by Django 4.1.4 on 2023-01-26 19:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0004_alter_project_date_create'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('surname',),
            },
        ),
        migrations.CreateModel(
            name='WorkerForProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 1, 26, 20, 27, 15, 505285))),
                ('hours_amount', models.PositiveIntegerField(default=0)),
                ('price_per_hour', models.FloatField(default=0, max_length=10)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('worker', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='workers.worker')),
            ],
        ),
    ]
