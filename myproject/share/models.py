from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.


class Upload(models.Model):
    visits = models.IntegerField(verbose_name='visits', default=0)
    file_code = models.CharField(max_length=8, verbose_name='code')
    datetime = models.DateTimeField(default=timezone.now, verbose_name='added time')
    path = models.CharField(max_length=32, verbose_name='download path')
    name = models.CharField(max_length=32, verbose_name='file name', default="")
    file_size = models.CharField(max_length=10, verbose_name='file size')
    ip = models.CharField(max_length=32, verbose_name='ip address', default="")

    """
    class Meta:
        verbose_name = "download"
        db_table = "download"
    """

    def __str__(self):
        return self.name
