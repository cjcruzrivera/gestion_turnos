
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
            cliente = Cliente.objects.filter(cedula=identificacion)
            if not cliente.exists():
                Cliente.objects.create(cedula=identificacion)

            if cliente.exists() and cliente.get().vip:
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
        servicios = Servicio.objects.all()
        return render(request, "turno/service_request.html", {'identificacion': identificacion, 'servicios': servicios})
    else:
        servicio_id = request.POST.get('servicio')
        cliente = Cliente.objects.get(cedula=identificacion)
        turno = Turno.objects.create(cliente_id=cliente.id, servicio_id=servicio_id, sucursal_id=request.user.sucursal.codigo, cajero_id=request.user.id)
        turno.turno = turno.servicio.tipo.nombre + str(turno.id)
        turno.save()
        return HttpResponseRedirect(reverse('turno', kwargs={'identificacion': turno.id}))
        # Llenar el turno y redireccionar a la vista de visualizacion de un turno


def TurnoView(request, identificacion):
    turno = Turno.objects.get(pk=identificacion)
    return render(request, "turno/turno_view.html", {'identificacion': identificacion, 'turno': turno})
    
