# Generated by Django 2.0 on 2019-06-14 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LizhiAccuMission',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('0', '未解决'), ('1', '已解决'), ('2', '无问题')], max_length=30)),
            ],
            options={
                'db_table': 'lizhi_accu_mission',
            },
        ),
        migrations.CreateModel(
            name='LizhiAccuResult',
            fields=[
                ('query_id', models.AutoField(primary_key=True, serialize=False)),
                ('query', models.CharField(max_length=1024)),
                ('sogou_res', models.CharField(max_length=107374)),
                ('baidu_res', models.CharField(max_length=107374)),
                ('sogou_pic', models.CharField(max_length=107374)),
                ('baidu_pic', models.CharField(max_length=107374)),
                ('precision', models.CharField(choices=[('0', '错误的case'), ('1', '需要改进的case'), ('2', '效果正常的case')], max_length=30)),
                ('status', models.CharField(choices=[('0', '未解决'), ('1', '已解决'), ('2', '无问题')], max_length=30)),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lizhi_accu_compare.LizhiAccuMission')),
            ],
            options={
                'db_table': 'lizhi_accu_result',
            },
        ),
    ]
