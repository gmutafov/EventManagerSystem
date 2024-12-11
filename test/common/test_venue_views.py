from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from eventManager.common.models import Venue, Organizer

UserModel = get_user_model()


class VenueViewsTest(TestCase):

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

    def test__staff_create_venue__expect_redirect(self):
        self.client.login(username='staffuser', password='12staff34')

        response = self.client.post(reverse('create-venue'), data={
            'name': 'Test Second Venue',
            'location': 'Test Second City',
            'capacity': 10,
            'available_from': '2024-12-01'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Venue.objects.count(), 2)

    def test__non_staff_user_create_venue__expect_unauthorized(self):
        self.client.login(username='normaluser', password='12test34')

        response = self.client.post(reverse('create-venue'))

        self.assertEqual(response.status_code, 403)
        self.assertEqual(Venue.objects.count(), 1)

    def test__delete_venue_by_staff_user__expect_redirect_to_success_page(self):
        self.client.login(username='staffuser', password='12staff34')

        response = self.client.post(reverse('delete-venue', args=[self.venue.pk]))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Venue.objects.count(), 0)
        self.assertFalse(Venue.objects.filter(pk=self.venue.pk).exists())

    def test__delete_venue_by_non_staff_user__expect_unauthorized(self):
        self.client.login(username='normaluser', password='12test34')

        response = self.client.post(reverse('delete-venue', args=[self.venue.pk]))

        self.assertEqual(response.status_code, 403)
        self.assertEqual(Venue.objects.count(), 1)
        self.assertTrue(Venue.objects.filter(pk=self.venue.pk).exists())



class OrganizerViewsTest(TestCase):

    def setUp(self):
        self.staff_user = UserModel.objects.create_user(
            username='staffuser', password='12staff34', email='staff@test.com', is_staff=True
        )
        self.normal_user = UserModel.objects.create_user(
            username='normaluser', password='12test34', email='normal@test.com', is_staff=False
        )

        self.organizer = Organizer.objects.create(
            name="Test Organizer",
            contact_info="organizer@example.com"
        )

    def test__staff_create_organizer__expect_redirect_success(self):
        self.client.login(username='staffuser', password='12staff34')

        response = self.client.post(reverse('create-organizer'), data={
            "name": "Test Organizer",
            "contact_info": "organizer@example.com"
        })


        self.assertEqual(response.status_code, 302)
        self.assertEqual(Organizer.objects.count(), 2)


    def test__non_staff_user_create_organizer__expect_unauthorized(self):
        self.client.login(username='normaluser', password='12test34')

        response = self.client.post(reverse('create-organizer'))

        self.assertEqual(response.status_code, 403)
        self.assertEqual(Organizer.objects.count(), 1)

    def test__delete_organizer_by_staff_user__expect_redirect_to_success_page(self):
        self.client.login(username='staffuser', password='12staff34')

        response = self.client.post(reverse('delete-organizer', args=[self.organizer.pk]))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Organizer.objects.count(), 0)
        self.assertFalse(Organizer.objects.filter(pk=self.organizer.pk).exists())

    def test__delete_organizer_by_non_staff_user__expect_unauthorized(self):
        self.client.login(username='normaluser', password='12test34')

        response = self.client.post(reverse('delete-organizer', args=[self.organizer.pk]))

        self.assertEqual(response.status_code, 403)
        self.assertEqual(Organizer.objects.count(), 1)
        self.assertTrue(Organizer.objects.filter(pk=self.organizer.pk).exists())


