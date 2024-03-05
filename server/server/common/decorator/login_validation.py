import json
from django.http import HttpResponseForbidden


def validate_login_request(func):
    def decorated(request, *args, **kwargs):
        data = json.loads(request.body)

        if not data['userId'] or not data['password']:
            return HttpResponseForbidden()

        return func(request, *args, **kwargs)
    return decorated

