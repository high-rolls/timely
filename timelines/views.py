from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Timeline, Event

def index(request):
    context = {
        'timelines': Timeline.objects.all().order_by('-created_date'),
    }
    return render(request, 'timelines/index.html', context=context)

def timeline(request, timeline_id):
    context = {
        'timeline': Timeline.objects.get(pk=timeline_id),
        'events': Event.objects.filter(timeline=timeline_id).order_by('start_date'),
    }
    return render(request, 'timelines/timeline.html', context=context)

def event(request, event_id):
    return HttpResponse("Hello from event %s!" % event_id)

def add_timeline(request):
    timeline = Timeline(name="Test Timeline", description="A test timeline")
    timeline.save()
    return HttpResponse("Added timeline %s!" % timeline.id)