from django.db import models
from enum import Enum
from .dashboard_list import DashboardList


class DelYn(Enum):
    Y = 'Y'
    N = 'N'


class DashboardPage(models.Model):
    id = models.BigIntegerField()
    dashboard_id = models.ForeignKey(DashboardList, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    del_yn = models.CharField(max_length=20, choices=[(tag, tag.value) for tag in DelYn])
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        app_label = 'hyper_report'
        db_table = 'dashboard_page'
