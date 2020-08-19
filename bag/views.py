from django.shortcuts import render

def view_bag(request):
    """ This view returns the Bag contents page """

    return render(request, 'bag/bag.html')
