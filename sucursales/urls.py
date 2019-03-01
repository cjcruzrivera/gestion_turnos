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
from .views import SucursalListView, SucursalCreateView, SucursalUpdateView, SucursalDeleteView

# TODO: personalizar urlpatterns para modificar names
urlpatterns = [
    path('', SucursalListView.as_view(), name='list_sucursales'),
    path('create/', SucursalCreateView.as_view(), name='create_sucursales'),
    path('update/<int:pk>', SucursalUpdateView.as_view(), name='update_sucursales'),
    path('delete/<int:pk>', SucursalDeleteView.as_view(), name='delete_sucursales'),
    # TODO: SucursalDetailView
]