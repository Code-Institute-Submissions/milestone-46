from django.shortcuts import render

def index(request):
    """ This view returns the Index page """

    return render(request, 'home/index.html')
