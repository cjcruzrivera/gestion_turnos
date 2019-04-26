from django.urls import path
from turno.views import TurnoView, IDView, ServicioView


urlpatterns = [
    path('', IDView.as_view(), name='id_request'),
    path('service/<int:identificacion>', ServicioView , name='service_request'),
    path('turno/<int:identificacion>', TurnoView , name='turno'),
]