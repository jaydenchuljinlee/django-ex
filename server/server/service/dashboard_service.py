from ..repository.dashboard_repository import DashboardRepository
from django import db


class DashboardService(object):
    @staticmethod
    def get_dashboard_list(_tenant_no, _user_no):
        received_dashboard_list = DashboardRepository.get_received_dashboard_list(_tenant_no, _user_no)
        private_dashboard_list = DashboardRepository.get_private_dashboard_list(_tenant_no, _user_no)
        shared_dashboard_list = DashboardRepository.get_shared_dashboard_list(_tenant_no, _user_no)

        results = {
            'received': received_dashboard_list,
            'private': private_dashboard_list,
            'shared': shared_dashboard_list
        }

        db.connections.close_all()

        return results
