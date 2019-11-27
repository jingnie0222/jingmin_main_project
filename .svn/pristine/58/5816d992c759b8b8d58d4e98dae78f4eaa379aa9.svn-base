from django.db import models


# Create your models here.
class vr_query_mission(models.Model):
    mission_id = models.AutoField(primary_key=True)
    mission_type = models.CharField(choices=(('query_for_id', 'ID对应查询词'), ('multi_id_query', 'ID交叉查询词')),
                                    default='query_for_id', max_length=20)
    query_from = models.CharField(choices=(('wap', '无线'), ('web', '网页')), max_length=3)
    vrid_list = models.CharField(max_length=107374)
    query_count_is_contained = models.BooleanField(blank=True, default=False)
    query_count = models.IntegerField()
    query_count_for_7 = models.IntegerField()
    order = models.CharField(choices=(('', '无排序'), ('pv', 'pv排序'), ('pvnum', 'pv排序')),
                             default='', max_length=10)
    result_format = models.CharField(max_length=20)
    result_encode = models.CharField(max_length=10)
    user = models.CharField(max_length=50)
    result_url = models.CharField(max_length=200, blank=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True)
    mission_status = models.CharField(
        choices=(('Waiting', '等待中'), ('Running', '进行中'), ('Finish', '已结束'), ('Failed', '未成功')), default='Waiting',
        max_length=10)

    class Meta:
        db_table = 'vr_query_mission'

    objects = models.Manager()
