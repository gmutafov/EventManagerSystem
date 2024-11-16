from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from eventManager.events.forms import EventCreateForm, EventEditForm, EventDeleteForm, EventDetailsForm
from eventManager.events.models import Event, Registration


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


class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event-detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.get_object()

        # Pass registration status to the template
        if self.request.user.is_authenticated:
            context['is_registered'] = event.registrations.filter(user=self.request.user).exists()
        else:
            context['is_registered'] = False

        return context

class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events/event-list.html'
    context_object_name = 'events'
    paginate_by = 10

    def get_queryset(self):
        return Event.objects.all()


class EventRegistrationView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        event = get_object_or_404(Event, pk=pk)

        # Check if the user is already registered
        if Registration.objects.filter(user=request.user, event=event).exists():
            messages.warning(request, "You are already registered for this event.")
        else:
            # Create a new registration
            Registration.objects.create(user=request.user, event=event)
            messages.success(request, "You have successfully registered for this event!")

        return redirect('event_detail', pk=pk)


class EventUnregisterView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        event = get_object_or_404(Event, pk=pk)

        # Check if the user is registered
        registration = Registration.objects.filter(user=request.user, event=event).first()
        if registration:
            registration.delete()
            messages.success(request, "You have successfully unregistered from this event.")
        else:
            messages.warning(request, "You are not registered for this event.")

        return redirect('event_detail', pk=pk)