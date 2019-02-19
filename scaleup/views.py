from django.shortcuts import render
from scale_gen import users_random_scale
from scaleup/scale_data import user_list
# from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'scaleup/home.html', {})


def newscale(request):
    user = request.GET.get('user', '')
    scale = users_random_scale(user_list[user])
    return render(request, 'scaleup/newscale.html', {"scale": scale, "user": user})

def nextscale(request, user):
    scale = users_random_scale(user_list[user])
    return render(request, 'scaleup/newscale.html', {"scale": scale, "user": user})
