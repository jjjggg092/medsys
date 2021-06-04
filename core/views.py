from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def new_request(request):
    return render(request, 'core/new_request.html')
