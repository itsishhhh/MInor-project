
from django.urls import path, include
from interface import views
from . import views
urlpatterns = [
   path('', views.home, name='home'),
   path('index', views.index, name='index'),
   path('Registration', views.Registration, name='registration'),
   path('Update', views.Update, name='Update'),
]