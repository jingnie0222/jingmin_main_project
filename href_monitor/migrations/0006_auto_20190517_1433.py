# Generated by Django 2.0 on 2019-05-17 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vr_query', '0005_auto_20190517_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vr_query_mission',
            name='end_time',
            field=models.DateTimeField(blank=True, default=''),
        ),
    ]
