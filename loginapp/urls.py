from django.urls import path
from .views import register,username

urlpatterns=[
    path('',register,name="register"),
    path('usernames/',username,name="username")
]