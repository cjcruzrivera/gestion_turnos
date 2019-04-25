
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, TemplateView
from turno.models import Turno
from turno.forms import IdForm, ServiceForm
from clientes.models import Cliente
from servicio.models import Servicio
from django.urls import reverse, reverse_lazy
# Create your views here.





class IDView(TemplateView):
    template_name = 'turno/id_request.html'
    form_class = IdForm
    success_url = '/'

    def get (self, request): 
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = IdForm(request.POST)

        if form.is_valid():
            identificacion = form.cleaned_data['identificacion']
            cliente = Cliente.objects.filter(cedula=identificacion).exists()
            if not cliente:
                Cliente.objects.create(cedula=identificacion)

            if cliente and cliente.VIP:
                # El cliente existe por tanto el servicio es VIP
                # Crear el turno y redireccionar a show_turno
                pass
            else:
                #Redireccionar a seleccionar servicio
                return HttpResponseRedirect(reverse('service_request', kwargs={'identificacion': identificacion}))
                pass
            # persona = Persona.objects.filter(ci="12345678901").exists()
            # args = {'form': form , 'text': text}
            # return render (request, 'service_request.html', {'text': text})

        return HttpResponse('Error in form')



def ServicioView(request, identificacion):
    if request.method == "GET":
        return render(request, "turno/service_request.html", {'identificacion': identificacion})
    else:
        servicio_id = request.POST.get('servicio')
        servicio = Servicio.objects.get(codigo=servicio_id)
        cliente = Cliente.objects.get(cedula=identificacion)
        turno = Turno.objects.create(cliente=cliente, servicio=servicio)
        return HttpResponse(turno.turno)
        # Llenar el turno y redireccionar a la vista de visualizacion de un turno

class TurnoView(CreateView): 
    template_name = 'service_request.html'

    def get (self, request): 
        form =  ServiceForm 
        return redirect ('/' )


   
    #success_url = '/success.html' 