from django.db import models


# Create your models here.
class user_record(models.Model):
    fsid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    uid = models.CharField(max_length=100)
    uno = models.CharField(max_length=7)
    login_time = models.CharField(max_length=15, blank=True)
    logout_time = models.CharField(max_length=15, blank=True)

    objects = models.Manager()
