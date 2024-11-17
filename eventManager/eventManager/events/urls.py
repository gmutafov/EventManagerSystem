from django.urls import path, include
from eventManager.events import views

urlpatterns = [
    path('create/', views.EventCreateView.as_view(), name='create_event'),
    path('event-list/', views.EventListView.as_view(), name='event_list'),
    path('my-registered-events/', views.UserRegisteredEventsView.as_view(), name='user_registered_events'),
    path('<int:pk>/', include([
        path('', views.EventDetailView.as_view(), name='event_detail'),
        path('delete/', views.EventDeleteView.as_view(), name='event_delete'),
        path('edit/', views.EventUpdateView.as_view(), name='event_edit'),
        path('register/', views.EventRegistrationView.as_view(), name='event_register'),
        path('unregister/', views.EventUnregisterView.as_view(), name='event_unregister'),
    ])),
]
