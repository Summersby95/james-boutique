from django.shortcuts import render

# Create your views here.
def view_bag(request):
    """ Renders bag contents """

    return render(request, 'bag/bag.html')