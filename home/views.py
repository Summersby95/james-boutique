from django.shortcuts import render

# Create your views here.
def index(request):
    """ Return Index Page """
    
    return render(request, 'home/index.html')