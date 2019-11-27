from django.db import models


# Create your models here.
class MonitorNotice(models.Model):
    id = models.AutoField(primary_key=True)
    monitor_id = models.IntegerField(default=0)
    type = models.CharField(
        max_length=30,
        choices=(
            ('0', 'debug'),
            ('1', 'info'),
            ('2', 'warning'),
            ('3', 'error'),
            ('4', 'critical'),
        )
    )
    title = models.CharField(max_length=128)
    message = models.CharField(max_length=32768)
    monitor_from = models.CharField(max_length=32768)
    status = models.CharField(
        max_length=30,
        choices=(
            ('0', '正常'),
            ('1', '异常'),
        )
    )
    owner = models.CharField(max_length=128)
    module = models.CharField(max_length=128)
    comment = models.CharField(max_length=32768)
    create_time = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        db_table = 'monitor_notice'


class MonitorConfig(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)

    class Meta:
        db_table = 'monitor_config'

    objects = models.Manager()