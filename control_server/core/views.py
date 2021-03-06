from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
import rest_framework.viewsets

from core import models
from core import serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from control_server.core.serializers import UserSerializer


def index(request):
    if not request.user.is_authenticated():
        return redirect('login')

    # user = request.user
    # if Token.objects.filter(user=user):
    #     token = Token.objects.filter(user=user)[0]
    # else:
    #     token = Token.objects.create(user=user)

    return render(request, 'index.html',) #{'token'=token}


class CarViewSet(rest_framework.viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarSerializer

    # def create(self, request, *args, **kwargs):
    #     request.user.cars.create(**request.data)

        # request.data['user_id'] = request.user.id#UserSerializer(request.user).data
        # print(request.data)
        # request.data['user'] = UserSerializer(request.user).data
        # print(UserSerializer(request.user).data)
        # print(request.data)
        #
        # serializers.CarSerializer().create(request.data)
        # print(123)
        # self.get_serializer(data=request.data)
        # print(12332)

        # super(CarViewSet, self).create(request, *args, **kwargs)
        # return HttpResponse('created')
    # def create(self, request, *args, **kwargs):
    #     print(100500)
    #     # super()
    #     return HttpResponse('created')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return models.Car.objects.filter(user=self.request.user)


def get_user_data(request):
    return JsonResponse({'username': request.user.username, 'id': request.user.id})


# class UseRead(rest_framework.viewsets.ReadOnlyModelViewSet):
#     user = 123
#
# get_user_data = UseRead.as_view({'retrieve': 'retrieve'})
# get_user_list = UseRead.as_view({'retrieve': 'retrieve'})


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