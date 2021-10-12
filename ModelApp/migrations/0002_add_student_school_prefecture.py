# Generated by Django 3.1.7 on 2021-08-08 09:17

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ModelApp', '0001_add_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prefectures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'prefectures',
            },
        ),
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('prefecture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ModelApp.prefectures')),
            ],
            options={
                'db_table': 'schools',
            },
        ),
        migrations.AlterField(
            model_name='person',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 8, 9, 17, 45, 508778, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='person',
            name='update_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 8, 9, 17, 45, 508845, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('major', models.CharField(max_length=20)),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ModelApp.schools')),
            ],
            options={
                'db_table': 'students',
            },
        ),
    ]
