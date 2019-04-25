from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente

		fields = ['cedula','nombre','apellidos','vip']

		widgets = {
            'cedula' : forms.TextInput(attrs={'class':'form-control','id':'cedula', 'placeholder': 'Ingrese la cedula del cliente'}),
            'apellidos' : forms.TextInput(attrs={'class':'form-control','id':'apellidos', 'placeholder': 'Ingrese los apellidos del cliente'}),
            'nombre' : forms.TextInput(attrs={'class':'form-control','id':'nombre', 'placeholder': 'Ingrese el nombre del cliente'}),
            'vip' : forms.CheckboxInput(attrs={'class':'form-control','id':'vip', 'placeholder': 'El usuario es VIP?'}),
        }