from django import forms
from django.utils.translation import ugettext_lazy as _
from turno.models import Turno 


class IdForm (forms.Form): 
    Identificación= forms.CharField()


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



class TurnoForm(forms.ModelForm):

    class Meta:
        model = Turno
        fields = [
            'turno',
            'tipo_turno',
            'isAtendido',
          #  'cliente',
            'sucursal',
            
        ]
        labels={
            'turno' : 'Turno',
            'tipo_turno' : 'Tipo de Turno',
            'isAtendido' : 'Atendido',
          #  'cliente' : 'ID Cliente',
            'sucursal' : 'Sucursal',
        }

        widgets = {
            'turno'  : forms.TextInput(attrs={'class':'form-control'}) ,
            'tipo_turno': forms.Select(attrs={'class':'form-control'}),
            'isAtendido' : forms.TextInput(attrs={'class':'form-control'}),
        #    'cliente' :  forms.SelectDateWidget(
        #        years = range(1990, 2018),   attrs={'class':'datepicker'}),
            'sucursal' : forms.Select(attrs={'class':'form-control'}),
        }