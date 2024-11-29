from django.http import HttpResponseForbidden
from django.shortcuts import render


class AdminAccessMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and not (request.user.is_staff or request.user.is_superuser):
            return render(request, 'common/user-not-staff.html', status=403)

        response = self.get_response(request)
        return response