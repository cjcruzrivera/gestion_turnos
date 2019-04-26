""" Views Login"""
# -*- coding: utf-8 -*-

from django.views.generic import FormView, RedirectView

# Authentication imports
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

from django.urls import reverse_lazy

# Create your views here.

class LoginView(FormView):
    """ Login View"""
    form_class = AuthenticationForm
    template_name = "login/login.html"
    success_url = reverse_lazy("core:index")

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

class LogoutView(RedirectView):
    """ Logout View """
    url = '/login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
