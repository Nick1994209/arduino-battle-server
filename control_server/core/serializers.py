# coding: utf-8
from django.contrib.auth.models import User
from rest_framework import serializers
from core import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class CarSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.Car
