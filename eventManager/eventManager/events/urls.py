from django.urls import path, include
from eventManager.events import views

urlpatterns = [
    path('create/', views.EventCreateView.as_view(), name='create_event'),
    path('event-list/', views.EventListView.as_view(), name='event-list'),
    path('my-registered-events/', views.UserRegisteredEventsView.as_view(), name='user-registered-events'),
    path('<int:pk>/', include([
        path('', views.EventDetailView.as_view(), name='event-detail'),
        path('delete/', views.EventDeleteView.as_view(), name='event-delete'),
        path('edit/', views.EventUpdateView.as_view(), name='event-edit'),
        path('register/', views.EventRegistrationView.as_view(), name='event-register'),
        path('unregister/', views.EventUnregisterView.as_view(), name='event-unregister'),
    ])),
]
