
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import home, new_invitation

app_name = 'player'

urlpatterns = [
    path('home', home, name="home"),
    path('login', LoginView.as_view(template_name="player/login.html"), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('new_invitation', new_invitation, name="new_invitation")

]
