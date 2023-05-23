from django.urls import path

from . import views

app_name = 'timelines'
urlpatterns = [
    path('', views.index, name='index')
]
