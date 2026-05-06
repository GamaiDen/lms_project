from rest_framework import serializers
from .models import User, Payment
from materials.serializers import CourseBriefSerializer, LessonBriefSerializer


class PaymentSerializer(serializers.ModelSerializer):
    course = CourseBriefSerializer(read_only=True)
    lesson = LessonBriefSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'city', 'avatar', 'payments', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'phone', 'city', 'avatar']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
