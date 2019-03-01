from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Sucursal
from .forms import SucursalForm
# Create your views here.

class SucursalListView(ListView):
    model = Sucursal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context['usuario'] = usuario
        return context

class SucursalCreateView(CreateView):
    model = Sucursal
    form_class = SucursalForm
    success_url = reverse_lazy('list_sucursales')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context['usuario'] = usuario
        return context

class SucursalUpdateView(UpdateView):
    model = Sucursal
    form_class = SucursalForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('list_sucursales')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context['usuario'] = usuario
        return context

class SucursalDeleteView(DeleteView):
    model = Sucursal
    success_url = reverse_lazy('list_sucursales')

