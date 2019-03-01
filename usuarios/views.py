from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Usuario
from .forms import UsuarioForm
# Create your views here.

class UsuarioListView(ListView):
    model = Usuario

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context['usuario'] = usuario
        return context

class UsuarioCreateView(CreateView):
    model = Usuario
    success_url = reverse_lazy('list_usuarios')
    form_class = UsuarioForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context['usuario'] = usuario
        return context

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    # template_name_suffix = '_update_form'
    success_url = reverse_lazy('list_sucursales')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context['usuario'] = usuario
        return context


class UsuarioDeleteView(DeleteView):
    model = Usuario
    success_url = reverse_lazy('list_usuarios')

