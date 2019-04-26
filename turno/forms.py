from django import forms
from django.utils.translation import ugettext_lazy as _
from turno.models import Turno 


class IdForm (forms.Form): 
    identificacion = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))

class ServiceForm(forms.Form): 

    SERVICE_CHOICES = (
    (1, _("Registrarse")),
    (2, _("Transacción en Dólares")),
    (3, _("Importaciones y Exportaciones")),
    (4, _("General")),
    (5, _("Seguros")),
    (6, _("Salir"))
    )
    
    service= forms.ChoiceField(choices = SERVICE_CHOICES, label="", 
                                    initial='', widget=forms.Select(), required=True)


