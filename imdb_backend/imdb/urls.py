from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('movie/',views.movie,name='movie'),
    path('actor/',views.actor,name='actor'),
    path('director/',views.director,name='director'),
    path('analytics/',views.analytics,name='analytics'),
]
