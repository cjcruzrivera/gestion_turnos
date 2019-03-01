"""gestion_turnos URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import UsuarioListView, UsuarioCreateView, UsuarioDeleteView, UsuarioUpdateView

# TODO: personalizar urlpatterns para modificar names
urlpatterns = [
    path('', UsuarioListView.as_view(), name='list_usuarios'),
    path('create/', UsuarioCreateView.as_view(), name='create_usuarios'),
    path('update/<int:pk>', UsuarioUpdateView.as_view(), name='update_usuarios'),
    path('delete/<int:pk>', UsuarioDeleteView.as_view(), name='delete_usuarios'),
    # TODO: SucursalDetailView
]