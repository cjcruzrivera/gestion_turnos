
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect 
from django.http import HttpResponse
from django.views.generic import CreateView, TemplateView
from turno.models import Turno
from turno.forms import TurnoForm, IdForm, ServiceForm
from django.urls import reverse_lazy 
# Create your views here.





class IDView(TemplateView):
    template_name = 'turno/id_request.html'
    success_url = '/'

    def get (self, request): 
        form =  IdForm 
        return render (request, self.template_name, {'form': form})

    def post(self, request):
        form = IdForm(request.POST)
       
        if form.is_valid() : 
            text = form.cleaned_data['Identificación']
            args = {'form': form , 'text': text}
            return render (request, 'turno/service_request.html', {'text': text})
        
        else: HttpResponse('Error Finding Page')
       

class ServiceView(TemplateView) : 
    template_name = 'turno/service_request.html' 

    def get (self, request): 
        form = ServiceForm
        return render(request, self.template_name, {'form': form})

    #success_url= reverse_lazy ('service_request')



class TurnoView(CreateView): 
    template_name = 'service_request.html'

    def get (self, request): 
        form =  ServiceForm 
        return redirect ('/' )


   
    #success_url = '/success.html' 