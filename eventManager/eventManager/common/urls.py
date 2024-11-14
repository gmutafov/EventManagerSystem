from django.urls import path, include
from eventManager.common import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('failure/', views.FailureView.as_view(), name='failure'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('venues/', views.VenueListView.as_view(), name='venue_list'),
    path('venues/create/', views.VenueCreateView.as_view(), name='create_venue'),
    path('venues/update/<int:pk>/', views.VenueUpdateView.as_view(), name='edit_venue'),

    # Organizer URLs
    path('organizers/', views.OrganizerListView.as_view(), name='organizer_list'),
    path('organizers/create/', views.OrganizerCreateView.as_view(), name='create_organizer'),
    path('organizers/<int:pk>/', include([
        path('edit/', views.OrganizerUpdateView.as_view(), name='edit_organizer'),
        path('delete/', views.OrganizerDeleteView.as_view(), name='delete_organizer'),
    ]))
    ,
]
