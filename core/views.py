from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')
def index(request):
    """ Index """
    usuario = request.user
    return render(request, 'core/index.html', {'usuario': usuario, 'exists': True})
