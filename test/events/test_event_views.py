from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from eventManager.common.models import Venue, Organizer
from eventManager.events.models import Event, Registration

UserModel = get_user_model()


class EventViewsTests(TestCase):
    def setUp(self):
        self.staff_user = UserModel.objects.create_user(
            username='staffuser', password='12staff34', email='staff@test.com', is_staff=True
        )
        self.normal_user = UserModel.objects.create_user(
            username='normaluser', password='12test34', email='normal@test.com', is_staff=False
        )

        self.venue = Venue.objects.create(
            name="Test Venue",
            location="Test City",
            capacity=10,
            available_from="2024-12-01"
        )

        self.organizer = Organizer.objects.create(
            name="Test Organizer",
            contact_info="organizer@example.com"
        )

        self.event = Event.objects.create(
            title="Test Event",
            description="Event Description",
            location="Test Location",
            venue=self.venue,
            date="2024-12-15",
            created_by=self.staff_user,
            organizer=self.organizer
        )

    def test__event_creation_by_staff_user__expects_success_redirect(self):
        self.client.login(username='staffuser', password='12staff34')

        response = self.client.post(reverse('create-event'), data={
            'title': 'New Event',
            'description': 'New Description',
            'location': 'New Location',
            'venue': self.venue.id,
            'date': '2024-12-20',
            'organizer': self.organizer.id,
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Event.objects.count(), 2)
        self.assertEqual(Event.objects.last().title, 'New Event')

    def test__event_creation_by_non_staff_user__expects_403_forbidden(self):
        self.client.login(username='normaluser', password='12test34')

        response = self.client.post(reverse('create-event'), data={
            'title': 'Test Event',
            'description': 'Test Description',
            'location': 'Test Location',
            'venue': self.venue.id,
            'date': '2024-12-20',
            'organizer': self.organizer.id,
        })

        self.assertEqual(response.status_code, 403)
        self.assertEqual(Event.objects.count(), 1)

    def test__user_registration_for_event__expects_redirect(self):
        self.client.login(username='normaluser', password='12test34')

        response = self.client.post(reverse('event-register', args=[self.event.pk]))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('event-detail', args=[self.event.pk]))

    def test__anonymous_user_register_for_event__expect_redirect_to_login_page(self):
        response = self.client.post(reverse('event-register', args=[self.event.pk]))
        self.assertEqual(response.status_code, 302)


    def test__user_unregister_for_event__expect_redirect(self):
        self.client.login(username='normaluser', password='12test34')

        response = self.client.post(reverse('event-unregister', args=[self.event.pk]))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('event-detail', args=[self.event.pk]))

