from django.urls import path
from .views import PublicidadCreateView

urlpatterns = [
    path('create/', PublicidadCreateView.as_view(), name='create_publicidad'),
]
