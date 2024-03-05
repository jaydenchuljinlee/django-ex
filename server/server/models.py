from django.db import models
from enum import Enum

class ViewType(Enum):
    L2: 'L2'
    L4: 'L4'


class DelYn(Enum):
    Y = 'Y'
    N = 'N'


class DashboardList(models.Model):
    id = models.BigAutoField(primary_key=True)
    tenant_no = models.BigIntegerField()
    user_no = models.BigIntegerField()
    user_no_sb = models.CharField(max_length=128)
    view_type = models.CharField(max_length=20, choices=[(tag, tag.value) for tag in ViewType])
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    del_yn = models.CharField(max_length=20, choices=[(tag, tag.value) for tag in DelYn])
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        app_label = 'hyper_report'
        db_table = 'dashboard_list'


class SharedDashboard(models.Model):
    dashboard_id = models.ForeignKey(DashboardList, related_name="dashboard", db_column="dashboard_id",
                                     on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    tenant_no = models.BigIntegerField()
    user_no = models.BigIntegerField()
    user_no_sb = models.CharField(max_length=128)
    del_yn = models.CharField(max_length=20, choices=[(tag, tag.value) for tag in DelYn])
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        app_label = 'hyper_report'
        db_table = 'shared_dashboard'
