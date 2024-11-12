from django.views.generic import ListView, TemplateView
from eventManager.events.models import Event
from datetime import date

class HomePageView(ListView):
    model = Event
    template_name = "common/home-page.html"
    context_object_name = "events"
    paginate_by = 3

    def get_queryset(self):
        return Event.objects.filter(date__gte=date.today()).order_by("date")

class SuccessView(TemplateView):
    template_name = 'common/success-page.html'

class FailureView(TemplateView):
    template_name = 'common/error-page.html'


class AboutPageView(TemplateView):
    template_name = 'common/about.html'


