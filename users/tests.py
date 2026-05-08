from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from materials.models import Course
from .models import User, Subscription


class SubscriptionTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@test.com', username='test', password='test12345')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(name='Test Course', description='Desc')
        self.sub_url = reverse('subscription')

    def test_subscribe(self):
        response = self.client.post(self.sub_url, {'course_id': self.course.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('подписка добавлена', response.data['message'])
        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())

    def test_unsubscribe(self):
        Subscription.objects.create(user=self.user, course=self.course)
        response = self.client.post(self.sub_url, {'course_id': self.course.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('подписка удалена', response.data['message'])
        self.assertFalse(Subscription.objects.filter(user=self.user, course=self.course).exists())


class PermissionTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@test.com', username='test', password='test12345')
        self.course = Course.objects.create(name='Test Course', description='Desc')
        self.lesson_url = reverse('lesson-list-create')

    def test_create_lesson_unauthorized(self):
        response = self.client.post(self.lesson_url, {'name': 'L1', 'course': self.course.pk})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_lesson_authorized(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.lesson_url, {
            'name': 'L1', 'description': 'D1',
            'video_url': 'https://youtube.com/1', 'course': self.course.pk
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
