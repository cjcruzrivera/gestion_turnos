from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Publicidad
from .forms import PublicidadForm

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

def mostrar_publicidad(request):
    queryset = Publicidad.objects.all()
    context = {
        "publicidad": queryset,
    }
    return render(request, 'publicidad/mostrar_publicidad.html', context)

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

'''
def upload_publicidad_view(request):
    if request.method == 'POST':
        form = PublicidadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "Imagen guardada exitosamente"
    
    else:
        form = PublicidadForm()

    return render_to_response('templates/publicidad/publicidad_form.html', locals(),
        context_instance = RequestContext(request))
'''