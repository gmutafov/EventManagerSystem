from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, UpdateView, CreateView, DeleteView

from eventManager.common.forms import OrganizerForm, VenueForm
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
    template_name = 'venue/venues-list.html'
    context_object_name = 'venues'

class OrganizerListView(ListView):
    model = Organizer
    template_name = 'organizer/organizers-list.html'
    context_object_name = 'organizers'

class VenueUpdateView(UpdateView):
    model = Venue
    form_class = VenueForm
    template_name = 'venue/venue-edit.html'
    success_url = reverse_lazy('venue-list')

class OrganizerUpdateView(UpdateView):
    model = Organizer
    form_class = OrganizerForm
    template_name = 'organizer/organizer-edit.html'
    success_url = reverse_lazy('organizer_list')


class VenueCreateView(CreateView):
    model = Venue
    form_class = VenueForm
    template_name = 'venue/venue-create.html'
    success_url = reverse_lazy('success')

class OrganizerCreateView(CreateView):
    model = Organizer
    form_class = OrganizerForm
    template_name = 'organizer/organizer-create.html'
    success_url = reverse_lazy('success')


class OrganizerDeleteView(DeleteView):
    model = Organizer
    template_name = 'organizer/organizer-delete.html'
    success_url = reverse_lazy('success')


class VenueDeleteView(DeleteView):
    model = Venue
    template_name = 'venue/venue-delete.html'
    success_url = reverse_lazy('success')