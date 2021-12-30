from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('travel', views.photo, name='photo'),
    path('travel_page', views.travel_page, name='travel_page')
    
]