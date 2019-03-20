from django.urls import path
from .views import PublicidadListView
from .views import PublicidadCreateView
from .views import PublicidadUpdateView
from .views import PublicidadDeleteView

urlpatterns = [
    path('', PublicidadListView.as_view(), name='list_publicidad'),
    path('create/', PublicidadCreateView.as_view(), name='create_publicidad'), 
    path('update/', PublicidadUpdateView.as_view(), name='update_publicidad'),   
    path('delete/<int:pk>', PublicidadDeleteView.as_view(), name='delete_publicidad'),
]
