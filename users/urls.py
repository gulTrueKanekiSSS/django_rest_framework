from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from users.views import PaymentListAPIView

app_name = 'users'

urlpatterns = [
    path('payment_list/', PaymentListAPIView.as_view(), name='payment_list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]