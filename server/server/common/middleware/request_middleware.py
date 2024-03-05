import json

from ..session.auth_context import ThreadLocalSingleton


class RequestMiddleware:
    auth_excluded_check_list = [
        "/api/v1/common/login",
        "/api/v1/common/token/refresh",
        "/api/v1/common/authentication/email",
        "/api/v1/common/view",
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # print("Request method:", request.method)
        # print("Request path:", request.path)

        for i in range(len(self.auth_excluded_check_list)):
            if self.auth_excluded_check_list[i] in request.path:
                return self.get_response(request)

        # authorization = request.headers.get("Authorization")
        authorization = 'token'
        if authorization == '':
            raise Exception("ACCESS_TOKEN_IS_NULL")

        # response = HyperReportApiMain().do_forward_get(GET_LOGIN_USER_INFO, authorization)
        user_info = {
            'tenant': 2,
            'id': 60
        }
        # user_info = json.loads(response.content)
        user_info['access_token'] = authorization

        ThreadLocalSingleton().set_data(user_info)
        # print("middleware")
        # print(ThreadLocalSingleton())
        return self.get_response(request)
