from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'scaleup/home.html', {})


def newscale(request):
    return render(request, 'scaleup/newscale.html', {})
    