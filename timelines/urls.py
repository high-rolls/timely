from django.urls import path

from . import views

app_name = 'timelines'
urlpatterns = [
    path('', views.index, name='index'),
    path('timeline/<int:timeline_id>/', views.timeline, name='timeline'),
    path('timeline/create', views.create_timeline, name='create_timeline'),
    path('timeline/edit/<int:timeline_id>/', views.edit_timeline, name='edit_timeline'),
    path('timeline/delete/<int:timeline_id>/', views.delete_timeline, name='delete_timeline'),
    path('timeline/<int:timeline_id>/create_event/', views.create_event, name='create_event'),
    path('event/<int:event_id>/', views.event, name='event'),
    path('event/edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('event/delete/<int:event_id>/', views.delete_event, name='delete_event'),
]
