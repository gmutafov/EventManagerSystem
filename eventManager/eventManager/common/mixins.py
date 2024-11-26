from django.http import HttpResponseForbidden


class NotAuthorizedMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("You are not authorized to access this page.")
        return super().dispatch(request, *args, **kwargs)