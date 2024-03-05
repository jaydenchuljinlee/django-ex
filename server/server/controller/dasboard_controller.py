from django.http import HttpResponse

import json
from ..common.session.auth_context import ThreadLocalSingleton
from ..service import dashboard_service


def get_dashboard_list(request):
    user_info = ThreadLocalSingleton().get_data()
    # print("controller")
    # print(ThreadLocalSingleton())
    tenantNo = user_info['tenant']
    userNo = user_info['id']
    results = dashboard_service.DashboardService.get_dashboard_list(tenantNo, userNo)
    # print(results)
    return HttpResponse(json.dumps(results, default=str), content_type='application/json')
