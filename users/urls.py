from django.urls import path
from . import views


urlpatterns = [
    path("signUp/", views.sign_up),
    path("signIn/", views.sign_in),
    path('dashboard/', views.dashboard)
]