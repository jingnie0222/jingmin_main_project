# Generated by Django 2.0 on 2019-09-18 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonitorNotice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('0', 'debug'), ('1', 'info'), ('2', 'warning'), ('3', 'error'), ('4', 'critical')], max_length=30)),
                ('title', models.CharField(max_length=128)),
                ('message', models.CharField(max_length=32768)),
                ('monitor_from', models.CharField(max_length=32768)),
                ('status', models.CharField(choices=[('0', '刚创建'), ('1', '已读'), ('2', '已处理')], max_length=30)),
                ('owner', models.CharField(max_length=128)),
                ('module', models.CharField(max_length=128)),
                ('comment', models.CharField(max_length=32768)),
            ],
        ),
    ]