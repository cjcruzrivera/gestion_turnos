from django import forms

from .models import Sucursal
class SucursalForm(forms.ModelForm):
    
    class Meta:
        model = Sucursal
        
        fields = ['codigo', 'nombre', 'direccion', 'localidad', 'telefono', 'tipo']
        
        labels = {'direccion' : 'Dirección'}

        widgets = {
            'codigo' : forms.TextInput(attrs={'class':'form-control','id':'codigo', 'placeholder': 'Ingrese el codigo de la sucursal'}),
            'nombre' : forms.TextInput(attrs={'class':'form-control','id':'nombre', 'placeholder': 'Ingrese el nombre de la sucursal'}),
            'direccion' : forms.TextInput(attrs={'class':'form-control','id':'direccion', 'placeholder': 'Ingrese la direccion de la sucursal'}),
            'localidad' : forms.TextInput(attrs={'class':'form-control','id':'localidad', 'placeholder': 'Ingrese la localidad de la sucursal'}),
            'telefono' : forms.TextInput(attrs={'class':'form-control','id':'telefono', 'placeholder': 'Ingrese el telefono de la sucursal'}),
            'tipo' : forms.Select(attrs={'class':'form-control','id':'tipo', 'placeholder': 'Ingrese el tipo de la sucursal'}),
        }