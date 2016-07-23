# coding: utf-8
from django.contrib.auth.models import User
from rest_framework import serializers
from core import models


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    cars = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Car.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'cars')


class CarSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = models.Car
        # fields = ('name', 'address', 'user', 'id')
