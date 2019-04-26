from django.views.generic import CreateView, TemplateView, ListView
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from turno.models import Turno
from clientes.models import Cliente
from clientes.forms import ClienteForm
from servicio.models import Servicio
# Create your views here.


def next_turno(request):
    cajero = request.user
    # Evaluar si hay turnos
    servicio = Servicio.objects.get(tipo_id=cajero.rol.id)
    turnos = Turno.objects.filter(isAtendido=False, hora_fin_turno__isnull=True,
                                  cajero__isnull=True, servicio_id=servicio.codigo).order_by('hora_solicitud')

    if not turnos:
        turnos = Turno.objects.filter(
            isAtendido=False, hora_fin_turno__isnull=True, cajero__isnull=True).order_by('hora_solicitud')
        if not turnos:
            return render(request, 'core/index.html', {'usuario': cajero, 'exists': False})

    turno = turnos.first()
    return HttpResponseRedirect(reverse('anteder_turno', kwargs={'turno': turno.id}))
    # try:
    # servicio = Servicio.objects.get(tipo_id=cajero.rol.id)
    # turnos = Turno.objects.filter(isAtendido=False, hora_fin_turno__isnull=True, cajero__isnull=False, servicio=servicio).order_by('hora_solicitud')
    # except Turno.DoesNotExist:
    # try:
    # turnos = Turno.objects.filter(isAtendido=False, hora_fin_turno__isnull=True, cajero__isnull=False, servicio=servicio).order_by('hora_solicitud')
    # except Turno.DoesNotExist:
    # return render(request, 'core/index.html', {'usuario': cajero, 'exists': False})


def AtenderTurnoView(request, turno):
    usuario = request.user
    turno = Turno.objects.get(pk=turno)
    cliente = turno.cliente
    form = ClienteForm()
    return render(request, 'cajero/atender_turno.html', {'form': form, 'usuario': usuario, 'turno': turno})

# class AtenderTurnoView(TemplateView):
    # template_name = 'cajero/atender_turno.html'
    # form_class = ClienteForm
    # success_url = '/'
#
    # def get(self, request):
    # form = self.form_class
    # return render(request, self.template_name, {'form': form})
