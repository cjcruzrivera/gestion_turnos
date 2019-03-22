
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.views.generic import CreateView, TemplateView
from turno.models import Turno
from turno.forms import TurnoForm, IdForm, ServiceForm
from django.urls import reverse
# Create your views here.


class IDView(TemplateView):
    template_name = 'turno/id_request.html'
    success_url = '/'
    form_class = IdForm

    def get (self, request): 
        form =  IdForm 
        return render (request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid(): 
            text = form.cleaned_data['identificacion']
            args = {'form': form , 'text': text}
            return render (request, 'service_request.html', {'text': text})

        else: HttpResponse('Error Finding Page')




class TurnoView(CreateView): 
    template_name = 'service_request.html'

    def get (self, request): 
        form =  ServiceForm 
        return redirect ('/' )


   
    #success_url = '/success.html' 