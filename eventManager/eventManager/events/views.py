from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from eventManager.events.forms import EventCreateForm, EventEditForm, EventDeleteForm, EventDetailsForm
from eventManager.events.models import Event


# Create your views here.

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventCreateForm
    template_name = 'events/create-event.html'
    success_url = reverse_lazy('success')  # Redirect to the event list page after success

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventEditForm
    template_name = 'events/edit-event.html'
    success_url = reverse_lazy('success')

    def get_queryset(self):
        return Event.objects.filter(created_by=self.request.user)


class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    form_class = EventDeleteForm
    template_name = 'events/delete-event.html'
    success_url = reverse_lazy('success')  # Redirect to the event list page after success

    def get_queryset(self):
        return Event.objects.filter(created_by=self.request.user)


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'events/event-detail.html'
    context_object_name = 'event'


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events/event-list.html'
    context_object_name = 'events'
    paginate_by = 10

    def get_queryset(self):
        return Event.objects.all()