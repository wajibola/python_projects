from django.test import TestCase

# Create your tests here.
from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a test user
        # self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_login_view_GET(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_view_POST_success(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertRedirects(response, '/catalogue', status_code=302, target_status_code=301)

    def test_login_view_POST_failure(self):
        response = self.client.post(reverse('login'), {'username': '', 'password': ''})
        self.assertEqual(response.status_code, 400)

    def test_catalogue_view(self):
        response = self.client.get(reverse('catalogue'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogue.html')
