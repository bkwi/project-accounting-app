# Generated by Django 4.1.4 on 2022-12-20 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('unit', models.CharField(choices=[('kg', 'kg'), ('mb', 'mb'), ('szt.', 'szt.')], help_text='jednostka', max_length=10)),
                ('amount', models.FloatField(default=0, null=True)),
                ('steel_type', models.CharField(choices=[('304', '304'), ('316', '316'), ('321', '321')], max_length=10)),
            ],
            options={
                'ordering': ('name',),
            },
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
    ]