from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'medsys/index.html')

def new_request(request):
    return render(request, 'medsys/new_request.html')
