from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('', views.newsletter_list, name='newsletter_list'),
]