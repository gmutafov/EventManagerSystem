from django.urls import path, include
from eventManager.common import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('failure/', views.FailureView.as_view(), name='failure'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('venue/', views.VenueListView.as_view(), name='venue_list'),
    path('venue/create/', views.VenueCreateView.as_view(), name='create_venue'),
    path('venue/<int:pk>/', include([
        path('edit/', views.VenueUpdateView.as_view(), name='edit_venue'),
        path('delete/', views.VenueDeleteView.as_view(), name='delete_venue'),
    ]))
    ,
    # Organizer URLs
    path('organizer/', views.OrganizerListView.as_view(), name='organizer_list'),
    path('organizer/create/', views.OrganizerCreateView.as_view(), name='create_organizer'),
    path('organizer/<int:pk>/', include([
        path('edit/', views.OrganizerUpdateView.as_view(), name='edit_organizer'),
        path('delete/', views.OrganizerDeleteView.as_view(), name='delete_organizer'),
    ]))
    ,
]
