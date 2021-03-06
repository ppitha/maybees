# Generated by Django 3.1 on 2020-08-15 22:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('start_datec', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Colony',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('queen_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('death_date', models.DateField()),
                ('description', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=100)),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='colony.colony')),
            ],
        ),
        migrations.CreateModel(
            name='Hive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField()),
                ('apiary_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='colony.apiary')),
            ],
        ),
        migrations.CreateModel(
            name='HiveColonyMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('colony_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='colony.colony')),
                ('hive_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='colony.hive')),
            ],
        ),
    ]
