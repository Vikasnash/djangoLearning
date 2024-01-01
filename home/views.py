from django.shortcuts import render  ## comes by default
from django.http import HttpResponse # need to import this
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.
# def home(request):
#     return HttpResponse('Hello, world!')

def home(request):
    return render(request, 'home/welcome.html', {'today': datetime.today()}) ## {} are arguments for html file

# @login_required  # block the access of user if not authorized
@login_required(login_url= '/admin')  ## give admin endpoint to lend up on this page if access is not there or we are not logged in
def authorized(request):
    return render(request, 'home/authorized.html', {}) ## {} are arguments for html file


