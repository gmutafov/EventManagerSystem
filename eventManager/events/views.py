from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from eventManager.common.mixins import StaffRequiredMixin
from eventManager.events.forms import EventCreateForm, EventEditForm, EventDeleteForm
from eventManager.events.models import Event, Registration



class EventCreateView(StaffRequiredMixin, LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventCreateForm
    template_name = 'events/create-event.html'
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class EventUpdateView(StaffRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventEditForm
    template_name = 'events/edit-event.html'
    success_url = reverse_lazy('success')


class EventDeleteView(StaffRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Event
    form_class = EventDeleteForm
    template_name = 'events/delete-event.html'
    success_url = reverse_lazy('success')


class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event-detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.get_object()
        registrations_count = Registration.objects.filter(event=event).count()
        remaining_capacity = event.venue.capacity - registrations_count
        context['remaining_capacity'] = remaining_capacity

        if self.request.user.is_authenticated:
            context['is_registered'] = event.registrations.filter(user=self.request.user).exists()
        else:
            context['is_registered'] = False

        return context

class EventListView(ListView):
    model = Event
    template_name = 'events/event-list.html'
    context_object_name = 'events'
    paginate_by = 10

    def get_queryset(self):
        return Event.objects.all()


class EventRegistrationView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        event = get_object_or_404(Event, pk=pk)
        registrations_count = Registration.objects.filter(event=event).count()

        if registrations_count >= event.venue.capacity:
            messages.warning(request, "This event is full. Registration is not allowed.")
        else:
            if Registration.objects.filter(user=request.user, event=event).exists():
                messages.warning(request, "You are already registered for this event.")
            else:
                Registration.objects.create(user=request.user, event=event)
                messages.success(request, "You have successfully registered for this event!")

        return redirect('event-detail', pk=pk)

class EventUnregisterView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        event = get_object_or_404(Event, pk=pk)

        registration = Registration.objects.filter(user=request.user, event=event).first()
        if registration:
            registration.delete()
            messages.success(request, "You have successfully unregistered from this event.")
        else:
            messages.warning(request, "You are not registered for this event.")

        return redirect('event-detail', pk=pk)


class UserRegisteredEventsView(LoginRequiredMixin, ListView):
    model = Registration
    template_name = "events/user-registered-events.html"
    context_object_name = "registrations"
    paginate_by = 5

    def get_queryset(self):
        return Registration.objects.filter(user=self.request.user).select_related('event')