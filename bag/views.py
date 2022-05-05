from django.shortcuts import render

def index(request):
    """ A view that renders the bag contents page"""

    return render(request, 'bag/bag.html') 