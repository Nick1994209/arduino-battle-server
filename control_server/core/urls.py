# coding: utf-8
from django.conf.urls import url, patterns
from rest_framework import routers

from core import views
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register('car', views.CarViewSet)


urlpatterns = [
    url(r'^$', views.index),
    url(r'^send_sprite_files_json$', views.send_sprite_files_json),

]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls
