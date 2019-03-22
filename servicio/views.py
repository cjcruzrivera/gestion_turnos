from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Servicio
from .forms import ServicioForm

class ServicioCreateView(CreateView):
    model = Servicio
    form_class = ServicioForm
    success_url = reverse_lazy('list_servicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context['usuario'] = usuario
        return context

class ServicioListView(ListView):
    model = Servicio
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context['usuario'] = usuario
        return context

class ServicioUpdateView(UpdateView):
    model = Servicio
    form_class = ServicioForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('list_servicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context['usuario'] = usuario
        return context

class ServicioDeleteView(DeleteView):
    model = Servicio
    success_url = reverse_lazy('list_servicio')