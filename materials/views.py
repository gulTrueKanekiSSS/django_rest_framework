from django.urls import path, include
from django_filters import OrderingFilter
from rest_framework import routers, viewsets, generics
from rest_framework.permissions import AllowAny

from materials.models import Lesson, Course
from materials.serializers import LessonSerializer, CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    authentication_classes = []
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonListAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDetailAPIView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateAPIView(generics.UpdateAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDeleteAPIView(generics.DestroyAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonCreateAPIView(generics.CreateAPIView):

    authentication_classes = []
    permission_classes = [AllowAny]

    serializer_class = LessonSerializer

