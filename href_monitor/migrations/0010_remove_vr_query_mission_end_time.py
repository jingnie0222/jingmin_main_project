# Generated by Django 2.0 on 2019-05-17 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vr_query', '0009_auto_20190517_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vr_query_mission',
            name='end_time',
        ),
    ]
