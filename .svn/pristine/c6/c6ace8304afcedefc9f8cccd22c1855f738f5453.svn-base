from django.db import models


# Create your models here.
class FrontPressModel(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=20)
    code = models.CharField(max_length=256)
    type = models.CharField(
        max_length=5,
        choices=(
            ('0', 'wap'),
            ('1', 'pc'),
        )
    )
    data_path = models.CharField(max_length=128)
    init_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=30,
        choices=(
            ('0', '刚提交'),
            ('1', '正在处理'),
            ('2', '处理完成'),
            ('3', '代码无法checkout'),
            ('4', '其他错误')
        )
    )
    result_url = models.CharField(max_length=256)
    result_summary = models.CharField(max_length=1048576)
    comment = models.CharField(max_length=8192)

    class Meta:
        db_table = 'front_press_mission'
