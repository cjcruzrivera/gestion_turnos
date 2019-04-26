from django.urls import path
from .views import TurnoListView, AtenderTurnoView

# TODO: personalizar urlpatterns para modificar names
urlpatterns = [
    path('', TurnoListView.as_view(), name='turnos_list'),
    path('atender/', AtenderTurnoView.as_view(), name='anteder_turno'),
    # TODO: SucursalDetailView
]