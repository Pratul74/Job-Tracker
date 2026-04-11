from django.urls import path
from .views import UserListView, UserRegisterView

urlpatterns=[
    path('list/', UserListView.as_view(), name='users-list'),
    path('register/', UserRegisterView.as_view(), name='register-user'),
]