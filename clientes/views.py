from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse

from .models import Cliente
from .forms import ClienteForm

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('list_cliente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context['usuario'] = usuario
        return context

class ClienteListView(ListView):
    model = Cliente
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context['usuario'] = usuario
        return context

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('list_cliente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context['usuario'] = usuario
        return context

class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('list_cliente')

def act_cliente(request):
    cedula = request.GET.get('cedula', None)
    nombre = request.GET.get('nombre', None)
    apellidos = request.GET.get('apellidos', None)
    vip = request.GET.get('vip', None)
    cliente = Cliente.objects.get(cedula=cedula)
    cliente.nombre = nombre
    cliente.apellidos = apellidos
    if vip:
        cliente.vip = True
    else:
        cliente.vip = False
    cliente.save()
    data = {
        'update': True
    }
    return JsonResponse(data)