from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.

from .models import Pet

def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {'pets':pets})


def pet_detail(request, id):
    try:
        pet = Pet.objects.get(id=id)
    except:
        raise Http404('Pet Not Found')
    return render(request, 'pet_detail.html', {'pet':pet})

