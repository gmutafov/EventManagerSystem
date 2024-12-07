from django.shortcuts import render, redirect


class StaffRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return render(request, 'common/user-not-staff.html', status=403)
        return super().dispatch(request, *args, **kwargs)