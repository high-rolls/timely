from django.http import HttpResponse, HttpResponseRedirect
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

def create_timeline(request):
    if request.method == 'POST':
        timeline = Timeline(name=request.POST['name'], description=request.POST['description'])
        timeline.save()
        return HttpResponse("Added timeline %s!" % timeline.id)
    return render(request, 'timelines/create_timeline.html')

def edit_timeline(request, timeline_id):
    if request.method == 'POST':
        timeline = Timeline.objects.get(pk=timeline_id)
        timeline.name = request.POST['name']
        timeline.description = request.POST['description']
        timeline.save()
        return HttpResponseRedirect(reverse('timelines:timeline', args=(timeline_id,)))
    return HttpResponse("Method not allowed!", status=405) # Method not allowed

def delete_timeline(request, timeline_id):
    if request.method == 'POST':
        Timeline.objects.get(pk=timeline_id).delete()
        return HttpResponseRedirect(reverse('timelines:index'))

def event(request, event_id):
    return HttpResponse("Hello from event %s!" % event_id)

def create_event(request, timeline_id):
    if request.method == 'POST':
        start_date = request.POST['start_date'] + ' ' + request.POST['start_time']
        end_date = request.POST['end_date'] + ' ' + request.POST['end_time']
        event = Event(
            timeline=Timeline.objects.get(pk=timeline_id),
            name=request.POST['name'],
            description=request.POST['description'],
            start_date=start_date,
            end_date=end_date,
        )
        event.save()
        return HttpResponseRedirect(reverse('timelines:timeline', args=(timeline_id,)))
    return render(request, 'timelines/create_event.html', context={'timeline_id': timeline_id})

def edit_event(request, event_id):
    if request.method == 'POST':
        event = Event.objects.get(pk=event_id)
        event.name = request.POST['name']
        event.description = request.POST['description']
        event.start_date = request.POST['start_date']
        event.end_date = request.POST['end_date']
        event.save()
        return HttpResponseRedirect(reverse('timelines:timeline', args=(event.timeline.id,)))

def delete_event(request, event_id):
    if request.method == 'POST':
        event = Event.objects.get(pk=event_id)
        timeline_id = event.timeline.id
        event.delete()
        return HttpResponseRedirect(reverse('timelines:timeline', args=(timeline_id,)))