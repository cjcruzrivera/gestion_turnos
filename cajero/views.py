from django.views.generic import CreateView, TemplateView, ListView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from turno.models import Turno
from clientes.models import Cliente
from clientes.forms import ClienteForm
# Create your views here.

class TurnoListView(ListView):
    model = Turno

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context['usuario'] = usuario
        return context

class AtenderTurnoView(TemplateView):
	template_name = 'cajero/atender_turno.html'
	form_class = ClienteForm
	success_url = '/'

	def get (self, request): 
		form = self.form_class
		return render(request, self.template_name, {'form': form})
# Create your views here.
