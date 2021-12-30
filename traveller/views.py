from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Destination
# Create your views here.


def index(request):
    return render(request, 'index.html')

def photo(request):

    dest2 = Destination.objects.all()
    return render(request, 'photography.html', {'dest2': dest2})

def travel_page(request):
    dests = Destination.objects.all()
    return render(request, 'travel_page.html', {'dests': dests})
