from django.urls import path, include
from rest_framework import routers

from materials import views
from materials.views import LessonListAPIView, LessonDetailAPIView, LessonUpdateAPIView, LessonDeleteAPIView

app_name = 'materials'

router = routers.DefaultRouter()
router.register(r'course', views.CourseViewSet, basename='course')

urlpatterns = [
    path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson-detail'),
    path('lesson_update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson_delete/<int:pk>/', LessonDeleteAPIView.as_view(), name='lesson-delete'),
    path('lesson_create/', views.LessonCreateAPIView.as_view(), name='lesson-create'),

] + router.urls