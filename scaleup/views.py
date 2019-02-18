from django.shortcuts import render
from violin_scale_generator import users_random_scale, lilit, beginner, test
# from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'scaleup/home.html', {})


def newscale(request, user):
    scale = users_random_scale(user)
    return render(request, 'scaleup/newscale.html', {"scale": scale})
    