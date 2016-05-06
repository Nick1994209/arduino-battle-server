# coding: utf-8
from auth2.forms import LoginForm, RegisterForm
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic import FormView


class Login(FormView):
    form_class = LoginForm
    template_name = 'auth2/login.html'

    def get_success_url(self):
        return reverse('core.views.index')

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

login = Login.as_view()


class Register(FormView):
    form_class = RegisterForm
    # success_url = "/login/"
    template_name = "auth2/register.html"

    def form_valid(self, form):
        user = form.save()
        user_cache = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password2'])
        auth.login(self.request, user_cache)
        return redirect('index')#('core.views.index')

register = Register.as_view()


def logout(request):
    redirect_to = 'login' #reverse('auth2.views.login')
    print(redirect_to)
    if not request.user.username:
        return redirect(redirect_to)
    auth.logout(request)

    return redirect(redirect_to)
