from django.urls import path
from .views import ApplicationListView, ApplicationCreateView

urlpatterns=[
    path('list/', ApplicationListView.as_view(), name='applications-list'),
    path('create/', ApplicationCreateView.as_view(), name='create-application'),
]