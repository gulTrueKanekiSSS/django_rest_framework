from django.test import TestCase
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from materials.models import Course, Lesson
from users.models import User, Subscription


class LessonTestCase(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(username=None, email='testuser', password='<PASSWORD>',)

        self.course = Course.objects.create(title='Test Course', description='Test Course')

        self.lesson_1 = Lesson.objects.create(name='Test Lesson 1', description='Test Lesson 1', course=self.course)

        self.lesson_2 = Lesson.objects.create(name='Test Lesson 2', description='Test Lesson 2', course=self.course)

        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        url = reverse_lazy('materials:lesson-create')
        data = {
            'name': 'Test Lesson 1',
            'description': 'Test Lesson 1',
            'course': self.course,
            'video_url': 'https://www.youtube.com/'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_lesson(self):
        url = f'/lesson_delete/{self.lesson_1.pk}/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_lesson(self):
        url = f'/lesson_update/{self.lesson_1.pk}/'
        data = {
            'name': 'Test Lesson 1',
            'description': 'Test Lesson 1',
            'course': self.course,
            'video_url': 'https://www.youtube.com/'
        }

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testDown(self):
        pass


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username=None, email='testuser', password='<PASSWORD>',)
        self.course = Course.objects.create(title='Test Course', description='Test Course')
        self.course2 = Course.objects.create(title='Test Course', description='Test Course')

        self.client.force_authenticate(user=self.user)

    def test_create_subscription(self):
        url = reverse_lazy('materials:subscription-create')
        data = {
            'user': self.user,
            'course': self.course,
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_subscription(self):
        subscription = Subscription.objects.create(user=self.user, course=self.course2, is_subscribed=True)
        url = reverse_lazy('materials:subscription-delete', args=[subscription.pk])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Subscription.objects.filter(user=self.user, course=self.course).exists())

    def tearDown(self):
        pass
