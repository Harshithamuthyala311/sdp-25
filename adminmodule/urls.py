from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.projecthomepage, name='projecthomepage'),
    path('properties/', views.propertieshomepage, name='propertieshomepage'),
    path('agents/', views.agentshomepage, name='agentshomepage'),
    path('signup', views.signup, name='signup'),  # Corrected to use a comma
    path('signup1', views.signup1, name='signup1'),
    path('login', views.login, name='login'),
    path('login1', views.login1, name='login1'),
    path('logout', views.logout, name='logout'),  # Corrected to use a comma
    # Add more URL patterns as needed
]
