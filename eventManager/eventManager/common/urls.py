from django.urls import path
from eventManager.common import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('failure/', views.FailureView.as_view(), name='failure'),
    path('about/', views.AboutPageView.as_view(), name='about'),
]