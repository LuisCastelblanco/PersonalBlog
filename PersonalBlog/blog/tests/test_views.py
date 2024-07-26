from django.test import TestCase
from django.contrib.auth.models import  User
from django.urls import reverse




class RegisterViewTest(TestCase):
    
    def test_register_view_post(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'redirect': 'blog'})
        self.assertTrue(User.objects.filter(username='testuser').exists())