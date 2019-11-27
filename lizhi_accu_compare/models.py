from django.db import models


# Create your models here.
class LizhiAccuMission(models.Model):
    task_id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=30,
        choices=(
            ('0', '未开始'),
            ('1', '进行中'),
            ('2', '已完成'),
        )
    )

    class Meta:
        db_table = 'lizhi_accu_mission'


class LizhiAccuResult(models.Model):
    query_id = models.AutoField(primary_key=True)
    task_id = models.ForeignKey(LizhiAccuMission, on_delete=models.DO_NOTHING)
    query = models.CharField(max_length=1024)
    sogou_res = models.CharField(max_length=107374)
    baidu_res = models.CharField(max_length=107374)
    sogou_pic = models.CharField(max_length=107374)
    baidu_pic = models.CharField(max_length=107374)
    precision = models.CharField(
        max_length=30,
        choices=(
            ('0', '未处理'),
            ('1', '错误'),
            ('2', '需要改进'),
            ('3', '效果正常'),
        )
    )
    status = models.CharField(
        max_length=30,
        choices=(
            ('0', '未解决'),
            ('1', '已解决'),
            ('2', '无问题'),
        )
    )
    solve_time = models.DateField(blank=True, null=True)
    comments = models.CharField(max_length=107374, blank=True, null=True, default='')
    edit_member = models.CharField(max_length=20, blank=True, null=True, default='')
    lizhi_type = models.CharField(
        max_length=30,
        default='0',
        choices=(
            ('0', '未标记'),
            ('1', '图谱'),
            ('2', 'VR'),
            ('3', '立知短答案'),
            ('4', '立知长答案'),
            ('5', '优质问答'),
        )
    )
    focus_member = models.CharField(max_length=100, blank=True, null=True, default='')
    edit_time = models.DateTimeField(blank=True, null=True)
    itest_record_title = models.CharField(max_length=100, blank=True, null=True, default='NULL')
    itest_record_id = models.CharField(max_length=20, blank=True, null=True, default='')


    class Meta:
        db_table = 'lizhi_accu_result'
