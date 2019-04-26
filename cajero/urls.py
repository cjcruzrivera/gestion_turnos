from django.urls import path
from .views import next_turno, AtenderTurnoView

# TODO: personalizar urlpatterns para modificar names
urlpatterns = [
    path('next/', next_turno, name="next_turno"),
    path('atender/<int:turno>', AtenderTurnoView, name='anteder_turno'),

]