from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect('core')
    return render(request, 'index.html')

def new_request(request):
    return render(request, 'core/new_request.html')
