from django.contrib.auth import login, get_user_model, logout
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from eventManager.accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from eventManager.accounts.models import AppUser
from eventManager.events.models import Registration


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        try:
            user = form.save()
            login(self.request, user)
            return redirect(self.success_url)
        except Exception as e:
            return redirect('failure')

class UserLoginView(LoginView):
    template_name = "registration/login.html"

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = AppUser
    template_name = 'profile/profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        if self.request.user.is_authenticated:
            return self.request.user
        raise Http404("No User found")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        registered_events_count = Registration.objects.filter(user=self.request.user).count()
        context['registered_events_count'] = registered_events_count
        return context

class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = AppUser
    form_class = CustomUserChangeForm
    template_name = 'profile/profile-edit.html'
    success_url = reverse_lazy('profile')  # Redirect to profile page after saving changes

    def get_object(self, queryset=None):
        return self.request.user  # Get the current logged-in user


class ProfileDeleteView(DeleteView):
    model = get_user_model()
    template_name = 'profile/profile-delete.html'
    context_object_name = 'user'
    success_url = reverse_lazy('home')  # Redirect to home page after successful deletion

    def get_object(self):
        return self.request.user  # Only the current logged-in user's profile can be deleted

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        logout(request)
        return HttpResponseRedirect(self.success_url)

