from abc import abstractstaticmethod

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, UpdateView, CreateView, DeleteView, DetailView

from eventManager.common.forms import OrganizerForm, VenueForm
from eventManager.common.mixins import StaffRequiredMixin
from eventManager.common.models import Venue, Organizer
from eventManager.events.models import Event
from datetime import date


class HomePageView(ListView):
    model = Event
    template_name = "common/home-page.html"
    context_object_name = "events"
    paginate_by = 3

    def get_queryset(self):
        queryset = Event.objects.filter(date__gte=date.today()).order_by("date")

        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(location__icontains=query)
            )
        return queryset

class SuccessView(TemplateView):
    template_name = 'common/success-page.html'


class FailureView(TemplateView):
    template_name = 'common/error-page.html'


class AboutPageView(TemplateView):
    template_name = 'common/about.html'


class VenueListView(StaffRequiredMixin, ListView):
    model = Venue
    template_name = 'venue/venues-list.html'
    context_object_name = 'venues'


class OrganizerListView(StaffRequiredMixin, ListView):
    model = Organizer
    template_name = 'organizer/organizers-list.html'
    context_object_name = 'organizers'


class VenueUpdateView(StaffRequiredMixin, UpdateView):
    model = Venue
    form_class = VenueForm
    template_name = 'venue/venue-edit.html'
    success_url = reverse_lazy('success')


class OrganizerUpdateView(StaffRequiredMixin, UpdateView):
    model = Organizer
    form_class = OrganizerForm
    template_name = 'organizer/organizer-edit.html'
    success_url = reverse_lazy('success')


class VenueCreateView(StaffRequiredMixin, CreateView):
    model = Venue
    form_class = VenueForm
    template_name = 'venue/venue-create.html'
    success_url = reverse_lazy('success')


class OrganizerCreateView(StaffRequiredMixin, CreateView):
    model = Organizer
    form_class = OrganizerForm
    template_name = 'organizer/organizer-create.html'
    success_url = reverse_lazy('success')


class OrganizerDeleteView(StaffRequiredMixin, DeleteView):
    model = Organizer
    template_name = 'organizer/organizer-delete.html'
    success_url = reverse_lazy('success')


class VenueDeleteView(StaffRequiredMixin, DeleteView):
    model = Venue
    template_name = 'venue/venue-delete.html'
    success_url = reverse_lazy('success')


class VenueDetailView(StaffRequiredMixin, DetailView):
    model = Venue
    template_name = 'venue/venue-details.html'
    context_object_name = 'venue'


class OrganizerDetailView(StaffRequiredMixin, DetailView):
    model = Organizer
    template_name = 'organizer/organizer-details.html'
    context_object_name = 'organizer'
