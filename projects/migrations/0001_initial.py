# Generated by Django 4.1.4 on 2023-01-06 16:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('address', models.CharField(max_length=300)),
                ('contact_person', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=240)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('unit', models.CharField(choices=[('kg', 'kg'), ('mb', 'mb'), ('szt.', 'szt.')], help_text='jednostka', max_length=10)),
                ('steel_type', models.CharField(choices=[('304', '304'), ('316', '316'), ('321', '321')], max_length=10)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ProductCreate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0, max_length=10)),
                ('price', models.FloatField(default=0, max_length=10)),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='projects.product')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
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
            name='WorkerWorkingTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 1, 6, 17, 27, 18, 661486))),
                ('hours_amount', models.PositiveIntegerField(default=0)),
                ('price_per_hour', models.FloatField(default=0, max_length=10)),
                ('worker', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='projects.worker')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCreate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0, max_length=10)),
                ('price', models.FloatField(default=0, max_length=10)),
                ('service', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='projects.service')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('date_create', models.DateTimeField(default=datetime.datetime(2023, 1, 6, 17, 27, 18, 664019))),
                ('ended', models.BooleanField(default=False)),
                ('client', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='projects.client')),
                ('products', models.ManyToManyField(related_name='projects', to='projects.productcreate')),
                ('services', models.ManyToManyField(related_name='projects', to='projects.servicecreate')),
                ('workers', models.ManyToManyField(related_name='projects', to='projects.workerworkingtime')),
            ],
        ),
    ]
