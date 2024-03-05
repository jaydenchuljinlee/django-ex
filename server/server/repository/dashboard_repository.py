from ..models import DashboardList
from ..models import SharedDashboard

class DashboardRepository:
    @staticmethod
    def get_received_dashboard_list(_tenant_no, _user_no):
        results = (SharedDashboard.objects
                   .filter(tenant_no=_tenant_no).filter(user_no=_user_no).filter(del_yn='N')
                   .select_related('dashboard_id')
                   .filter(dashboard_id__del_yn='N')
                   .values('dashboard_id__id', 'dashboard_id__title', 'dashboard_id__description'))

        return list(results)

    def get_private_dashboard_list(_tenant_no, _user_no):
        results = (DashboardList.objects
                   .filter(tenant_no=_tenant_no).filter(user_no=_user_no).filter(del_yn='N')
                   .values('id', 'title', 'description'))

        return list(results)

    def get_shared_dashboard_list(_tenant_no, _user_no):
        results = (SharedDashboard.objects
                   .filter(del_yn='N')
                   .select_related('dashboard_id')
                   .values('dashboard_id__id', 'dashboard_id__title', 'dashboard_id__description')
                   .filter(dashboard_id__tenant_no=_tenant_no).filter(dashboard_id__user_no=_user_no).filter(dashboard_id__del_yn='N'))

        return list(results)


import heapq

import heapq

