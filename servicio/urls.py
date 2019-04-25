from django.urls import path
from .views import ServicioListView
from .views import ServicioCreateView
from .views import ServicioUpdateView
from .views import ServicioDeleteView

urlpatterns = [
    path('', ServicioListView.as_view(), name='list_servicio'),
    path('create/', ServicioCreateView.as_view(), name='create_servicio'), 
    path('update/<int:pk>', ServicioUpdateView.as_view(), name='update_servicio'),   
    path('delete/<int:pk>', ServicioDeleteView.as_view(), name='delete_servicio'),
]
