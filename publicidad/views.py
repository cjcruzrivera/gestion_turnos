from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Publicidad
from .forms import PublicidadForm

from turno.models import Turno

class PublicidadCreateView(CreateView):
    model = Publicidad
    form_class = PublicidadForm
    success_url = reverse_lazy('list_publicidad')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context['usuario'] = usuario
        return context

class PublicidadListView(ListView):
    model = Publicidad
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context['usuario'] = usuario
        return context

class PublicidadTurno(ListView):
    model = Publicidad
    form_class = PublicidadForm
    template_name_suffix = '_mostrar'
    success_url = reverse_lazy('turno_publicidad')

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        turnos = Turno.objects.filter(isAtendido=False, hora_fin_turno__isnull=True, cajero__isnull=False)
        context['usuario'] = usuario
        context['turnos'] = turnos
        return context  

class PublicidadUpdateView(UpdateView):
    model = Publicidad
    form_class = PublicidadForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('list_publicidad')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context['usuario'] = usuario
        return context

class PublicidadDeleteView(DeleteView):
    model = Publicidad
    success_url = reverse_lazy('list_publicidad')
