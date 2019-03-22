from django.urls import path
from turno.views import TurnoView, IDView


urlpatterns = [
    path('id/', IDView.as_view(), name='id_request'),

]