from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from .models import Course, Lesson


class LessonCRUDTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@test.com', username='test', password='test12345')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(name='Test Course', description='Desc')
        self.lesson_url = reverse('lesson-list-create')
        self.lesson_data = {
            'name': 'Test Lesson',
            'description': 'Lesson description',
            'video_url': 'https://youtube.com/test',
            'course': self.course.pk,
        }

    def test_create_lesson(self):
        response = self.client.post(self.lesson_url, self.lesson_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.count(), 1)

    def test_get_lessons(self):
        Lesson.objects.create(name='L1', description='D1', video_url='https://youtube.com/1', course=self.course, owner=self.user)
        response = self.client.get(self.lesson_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_update_lesson(self):
        lesson = Lesson.objects.create(name='L1', description='D1', video_url='https://youtube.com/1', course=self.course, owner=self.user)
        url = reverse('lesson-detail', kwargs={'pk': lesson.pk})
        response = self.client.patch(url, {'name': 'Updated'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_lesson(self):
        lesson = Lesson.objects.create(name='L1', description='D1', video_url='https://youtube.com/1', course=self.course, owner=self.user)
        url = reverse('lesson-detail', kwargs={'pk': lesson.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_video_url(self):
        data = {**self.lesson_data, 'video_url': 'https://vimeo.com/test'}
        response = self.client.post(self.lesson_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
