from rest_framework import serializers

from materials.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    amount_of_lessons = serializers.SerializerMethodField()
    all_lessons = LessonSerializer(many=True, read_only=True)

    @staticmethod
    def get_amount_of_lessons(obj):
        return obj.lesson_set.count()

    class Meta:
        model = Course
        fields = '__all__'

