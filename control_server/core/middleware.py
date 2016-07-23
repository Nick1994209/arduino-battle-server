# coding: utf-8
from django.conf import settings
from project.settings import EXCLUDE_LOGIN_URLS
from django.shortcuts import redirect


class RequiredLogin(object):

    def process_request(self, request):
        if not request.user.is_authenticated():

            for path in EXCLUDE_LOGIN_URLS:
                if request.path.startswith(path):
                    return

            return redirect('login')