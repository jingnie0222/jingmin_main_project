# Generated by Django 2.0 on 2019-05-17 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vr_query', '0011_remove_vr_query_mission_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vr_query_mission',
            name='result_url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
