from django.test import TestCase
from django.utils import timezone
from .models import Timeline, Event

class TimelinesTestCase(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello from timely!")
    
    def test_timeline(self):
        response = self.client.get('/timeline/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello from timeline 1!")
    
    def test_event(self):
        response = self.client.get('/event/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello from event 1!")


class TimelineModelTestCase(TestCase):
    def test_str(self):
        timeline = Timeline(name="Test Timeline", description="A test timeline")
        self.assertEqual(str(timeline), "Test Timeline")


class EventModelTestCase(TestCase):
    def test_str(self):
        timeline = Timeline(name="Test Timeline", description="A test timeline")
        event = Event(timeline=timeline, name="Test Event", description="A test event", start_date=timezone.now(), end_date=timezone.now())
        self.assertEqual(str(event), "Test Event")
    
    def test_is_current(self):
        timeline = Timeline(name="Test Timeline", description="A test timeline")
        event = Event(timeline=timeline, name="Test Event", description="A test event", start_date=timezone.now(), end_date=timezone.now() + timezone.timedelta(days=1))
        self.assertTrue(event.is_current())
    
    def test_get_duration(self):
        timeline = Timeline(name="Test Timeline", description="A test timeline")
        event = Event(timeline=timeline, name="Test Event", description="A test event", start_date=timezone.now(), end_date=timezone.now() + timezone.timedelta(days=1))
        self.assertEqual(event.get_duration(), timezone.timedelta(days=1))