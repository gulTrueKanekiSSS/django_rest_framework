from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from users.models import Payments
from users.serializerz import PaymentSerializer


class PaymentListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'way_of_pay')
    ordering_fields = ('date_of_pay',)

