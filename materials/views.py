from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from materials.models import Lesson, Course
from materials.serializers import LessonSerializer, CourseSerializer, SubsriptionSerializer
from users.models import Subscription


class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonCreateAPIView(generics.CreateAPIView):

    permission_classes = [IsAuthenticated]

    serializer_class = LessonSerializer


class SubscriptionCreateAPIView(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubsriptionSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SubscriptionDeleteAPIView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
