from django.urls import path
from turno.views import TurnoView, IDView,ServiceView


urlpatterns = [
    path('id/', IDView.as_view(), name='id_request'),
    path('servicio/', ServiceView.as_view(), name= 'service_request'),

]