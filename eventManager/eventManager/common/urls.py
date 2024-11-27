from django.contrib.auth.decorators import user_passes_test
from django.urls import path, include
from eventManager.common import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('failure/', views.FailureView.as_view(), name='failure'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('venues/', views.VenueListView.as_view(), name='venue-list'),
    path('venue/create/', views.VenueCreateView.as_view(), name='create-venue'),
    path('venue/<int:pk>/', include([
        path('edit/', views.VenueUpdateView.as_view(), name='edit-venue'),
        path('delete/', views.VenueDeleteView.as_view(), name='delete-venue'),
        path('details/', views.VenueDetailView.as_view(), name='venue-details'),
    ]))
    ,
    # Organizer URLs
    path('organizers/', views.OrganizerListView.as_view(), name='organizer-list'),
    path('organizers/create/', views.OrganizerCreateView.as_view(), name='create-organizer'),
    path('organizer/<int:pk>/', include([
        path('details/', views.OrganizerDetailView.as_view(), name='organizer-details'),
        path('edit/', views.OrganizerUpdateView.as_view(), name='edit-organizer'),
        path('delete/', views.OrganizerDeleteView.as_view(), name='delete-organizer'),
    ]))
    ,
]
