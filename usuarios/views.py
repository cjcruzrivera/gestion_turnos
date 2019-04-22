from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

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
    success_url = reverse_lazy('list_usuarios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context['usuario'] = usuario
        return context

    def get_form_kwargs(self):
        kwargs = super(UsuarioUpdateView, self).get_form_kwargs()
        kwargs.update({'is_update': True})
        kwargs.update({'instance': Usuario.objects.get(pk=self.kwargs["pk"])})
        return kwargs


class UsuarioDeleteView(DeleteView):
    model = Usuario
    success_url = reverse_lazy('list_usuarios')

