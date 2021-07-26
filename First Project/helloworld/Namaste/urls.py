
from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePageViewNew, name='home'),
]
