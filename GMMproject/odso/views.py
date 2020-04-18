from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def map(request):
    return render(request, 'map.html')

def map2(request):
    return render(request, 'map2.html')