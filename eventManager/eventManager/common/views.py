from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, UpdateView, CreateView, DeleteView

from eventManager.common.forms import OrganizerForm, VenueForm, OrganizerDeleteForm
from eventManager.common.models import Venue, Organizer
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


class VenueListView(ListView):
    model = Venue
    template_name = 'venues/venues-list.html'
    context_object_name = 'venues'

class OrganizerListView(ListView):
    model = Organizer
    template_name = 'organizers/organizers-list.html'
    context_object_name = 'organizers'

class VenueUpdateView(UpdateView):
    model = Venue
    form_class = VenueForm
    template_name = 'venues/venue-edit.html'
    success_url = reverse_lazy('venues-list')

class OrganizerUpdateView(UpdateView):
    model = Organizer
    form_class = OrganizerForm
    template_name = 'organizers/organizer-edit.html'
    success_url = reverse_lazy('organizer_list')


class VenueCreateView(CreateView):
    model = Venue
    form_class = VenueForm
    template_name = 'venues/venue-create.html'
    success_url = reverse_lazy('venues_list')

class OrganizerCreateView(CreateView):
    model = Organizer
    form_class = OrganizerForm
    template_name = 'organizers/organizer-create.html'
    success_url = reverse_lazy('organizer_list')


class OrganizerDeleteView(DeleteView):
    model = Organizer
    form_class = OrganizerDeleteForm
    template_name = 'organizers/organizer-delete.html'
    success_url = reverse_lazy('success')
