from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import LessonVideoValidator
from users.models import Subscription


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LessonVideoValidator(field='video_url')]


class CourseSerializer(serializers.ModelSerializer):

    amount_of_lessons = serializers.SerializerMethodField()
    all_lessons = LessonSerializer(many=True, read_only=True)

    @staticmethod
    def get_amount_of_lessons(obj):
        return obj.lesson_set.count()

    class Meta:
        model = Course
        fields = '__all__'


class SubsriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
