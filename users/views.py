from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from materials.models import Course
from .models import User, Payment, Subscription
from .serializers import UserSerializer, PaymentSerializer, RegisterSerializer


class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method in ('PUT', 'PATCH'):
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['course', 'lesson', 'method']
    ordering_fields = ['payment_date']
    ordering = ['-payment_date']


class SubscriptionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        course_id = request.data.get('course_id')
        course = get_object_or_404(Course, pk=course_id)
        sub = Subscription.objects.filter(user=user, course=course)

        if sub.exists():
            sub.delete()
            return Response({"message": "подписка удалена"})
        else:
            Subscription.objects.create(user=user, course=course)
            return Response({"message": "подписка добавлена"})
