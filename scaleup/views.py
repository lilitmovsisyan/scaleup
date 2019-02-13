from django.shortcuts import render
from violin_scale_generator import users_random_scale, lilit
# from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'scaleup/home.html', {})


def newscale(request):
    scale = users_random_scale(lilit)
    return render(request, 'scaleup/newscale.html', {"scale": scale})
    