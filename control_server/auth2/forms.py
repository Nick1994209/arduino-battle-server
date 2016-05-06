# -*- coding:utf-8 -*-
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Логин")

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )

        return self.cleaned_data


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label=("Пароль"),
                                strip=False,
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Повторите пароль"),
                                widget=forms.PasswordInput,
                                strip=False,
                                help_text=("Пароли должны совподать"))

    class Meta:
        model = User
        fields = ("username",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                u'Пароли не совпадают',
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user