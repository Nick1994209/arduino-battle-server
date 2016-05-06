from django.http.response import JsonResponse
from django.shortcuts import render, redirect
import rest_framework.viewsets

from core import models
from core import serializers
from rest_framework.authtoken.models import Token


def index(request):
    if not request.user.is_authenticated():
        return redirect('login')

    user = request.user
    token = Token.objects.create(user=user)
    return render(request, 'index.html', {'token': token})


class CarViewSet(rest_framework.viewsets.ReadOnlyModelViewSet):
    queryset = models.Car.objects.all()
    serializer_class = serializers.Car


def send_sprite_files_json(request):

    dir_name = '/static/core/sprites/'
    static_files = {
        'images': {
                'balls': dir_name+'balls.png',
                'sprite_bullet_and_fire': dir_name+'sprite_bullet_and_fire.png'
        },
        'js': {
            "jsmpg": dir_name + 'jsmpg.js',
            "sprite2": dir_name + 'sprite2.js',
            "shot_sprite": dir_name + 'shot_sprite.js',
            "video_and_sprites": dir_name + 'video_and_sprites.js'
        }
    }

    return JsonResponse(static_files)