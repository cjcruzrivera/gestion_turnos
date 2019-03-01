from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Sucursal
# Create your views here.

class SucursalListView(ListView):
    model = Sucursal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context['usuario'] = usuario
        return context