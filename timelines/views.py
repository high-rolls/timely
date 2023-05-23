from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello from timely!")

def timeline(request, timeline_id):
    return HttpResponse("Hello from timeline %s!" % timeline_id)

def event(request, event_id):
    return HttpResponse("Hello from event %s!" % event_id)