from django.urls import path
from .views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView, act_cliente

urlpatterns = [
    path('', ClienteListView.as_view(), name='list_cliente'),
    path('create/', ClienteCreateView.as_view(), name='create_cliente'), 
    path('update/<int:pk>', ClienteUpdateView.as_view(), name='update_cliente'),   
    path('delete/<int:pk>', ClienteDeleteView.as_view(), name='delete_cliente'),
    path('act_ajax', act_cliente, name="act_cliente")
]
