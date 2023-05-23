from django.urls import path

from . import views

app_name = 'timelines'
urlpatterns = [
    path('', views.index, name='index'),
    path('timeline/<int:timeline_id>/', views.timeline, name='timeline'),
    path('event/<int:event_id>/', views.event, name='event')
]
